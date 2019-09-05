from newsapi.newsapi_client import NewsApiClient
import os
import twitter
import credentials
import json
from neo4j import GraphDatabase
from bs4 import BeautifulSoup
import requests
import urllib.request
import time

# driver = GraphDatabase.driver(
#     "bolt://localhost:7687", auth=("neo4j", "london"))

API_KEY = os.environ.get('NEWS_KEY')

# Innit
newsapi = NewsApiClient(api_key=(API_KEY))

# /v2/top-headlines
top_headlines = newsapi.get_everything(sources='reuters',
                                       domains='uk.reuters.com/news/',
                                       language='en')


API_CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
API_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
API_ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
API_ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


api = twitter.Api(consumer_key=(API_CONSUMER_KEY),
                  consumer_secret=(API_CONSUMER_SECRET),
                  access_token_key=(API_ACCESS_TOKEN_KEY),
                  access_token_secret=(API_ACCESS_TOKEN_SECRET),
                  sleep_on_rate_limit=True)

article_title = []

for article in top_headlines['articles']:
    article_title.append(article['title'])

article_title = list(set(article_title))

results = {}

for headline in article_title:
    results[headline] = api.GetSearch(
        term=headline, count=100, return_json=True)

output = {}

for k, v in results.items():
    users = []
    for i in v['statuses']:
        users.append(i['user']['screen_name'])
    output[k] = users

users_by_headline = []

for k, v in results.items():
    user_info = []
    for tweets in v['statuses']:
        user_info.append({'screen_name': tweets['user']['screen_name'],
                          'urls': tweets['user']['urls'],
                          'tweet_count': tweets['user']['statuses_count'],
                          'created_at': tweets['user']['created_at'],
                          'description': tweets['user']['description'],
                          'url': tweets['user']['entities']['urls']})
    users_by_headline.append(user_info)


def add_node_user(tx, headline, name):
    tx.run("MERGE (a:User {name: $name}) "
           "MERGE (h:Headline {headline: $headline}) "
           "MERGE (a)-[:RETWEETED]->(h)",
           name=name, headline=headline)


def print_nodes(tx):
    for record in tx.run("MATCH (n) RETURN n"):
        print(record)


with driver.session() as session:
    for k, v in output.items():
        for user in v:
            session.write_transaction(add_node_user, k, user)
    session.read_transaction(print_nodes)


def return_non_verified_nonprotected_users(results):
    for k, v in results.items():
        users = []
        for tweet in v['statuses']:
            if tweet['user']['verified'] == False and tweet['user']['protected'] == False :
                users.append(tweet['user']['screen_name'])
    return users

def find_fake_news_urls(user):
    for url in user['entities']['description']['urls']:
        print(url)
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        print(soup.prettify())
