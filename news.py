from newsapi import NewsApiClient
import os
import twitter
import credentials
import json
from neo4j import GraphDatabase

driver = GraphDatabase.driver(
    "bolt://localhost:7687", auth=("neo4j", "london"))

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
        raw_query="q={k}&count=100", return_json=True)

output = {}

for k, v in results.items():
    users = []
    print(len(v['statuses']))
    for i in v['statuses']:
        users.append(i['user']['screen_name'])
    output[k] = users


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
