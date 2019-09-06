import os
import twitter
import credentials
import json
import time
import news

# Init
API_CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
API_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
API_ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
API_ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


api = twitter.Api(consumer_key=(API_CONSUMER_KEY),
                  consumer_secret=(API_CONSUMER_SECRET),
                  access_token_key=(API_ACCESS_TOKEN_KEY),
                  access_token_secret=(API_ACCESS_TOKEN_SECRET),
                  sleep_on_rate_limit=True)


def twitter_search_headline():

    results = {}

    for headline in news.article_title:
        results[headline] = api.GetSearch(
            term=headline, count=100, return_json=True)
    return results


def twitter_search_headline_user():

    output = {}

    for k, v in results.items():
        users = []
        for i in v['statuses']:
            users.append(i['user']['screen_name'])
        output[k] = users


def twitter_search_users():

    users_by_headline = []
    results = twitter_search_headline()

    for k, v in results.items():
        user = {}
        for tweet in v['statuses']:
            user.update({'screen_name': tweet['user']['screen_name'],
                         'urls': tweet['entities']['urls'],
                         'verified': tweet['user']['verified'],
                         'protected': tweet['user']['protected'],
                         'created_at': tweet['user']['created_at'],
                         'statuses_count': tweet['user']['statuses_count'],
                         'description': tweet['user']['description']})
        if len(user.keys()) > 0:
            users_by_headline.append(user)

    # print(users_by_headline)
    return users_by_headline


def run_twitter_query():
    return twitter_search_users()


def output_users(query):
    users = []
    user = {}
    for tweet in query['statuses']:
        user.update({'screen_name': tweet['user']['screen_name'],
                     'urls': tweet['entities']['urls'],
                     'verified': tweet['user']['verified'],
                     'protected': tweet['user']['protected'],
                     'created_at': tweet['user']['created_at'],
                     'statuses_count': tweet['user']['statuses_count'],
                     'description': tweet['user']['description']})
        if len(user.keys()) > 0:
            users.append(user)
    return(users)


run_twitter_query()
