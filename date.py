from newsapi.newsapi_client import NewsApiClient
import os
import twitter
import credentials
import json
import time
import datetime


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
        term=headline, count=10, return_json=True)

users = []
for k, v in results.items():
    for tweet in v['statuses']:
        user = {}
        user.update({'screen_name': tweet['user']['screen_name'],
                     'urls': tweet['entities']['urls'],
                     'created_at': tweet['user']['created_at'],
                     'statuses_count': tweet['user']['statuses_count'],
                     'description': tweet['user']['description']})
        users.append(user)


def average_tweets_per_day(user):
    date_time_str = user['created_at']
    array_date = date_time_str.split(" ")
    del array_date[0]
    del array_date[3]
    list_date = ' '.join(array_date)
    date_object = datetime.datetime.strptime(
        list_date, '%b %d %H:%M:%S %Y').date()
    date = datetime.datetime.now().date()
    date2 = date - date_object
    date3 = int(str(date2).split(" ")[0])
    return int(user['statuses_count'])/date3


for user in users:
    if average_tweets_per_day(user) >= 240:
        print(average_tweets_per_day(user))
