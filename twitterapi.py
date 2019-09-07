import os
import twitter
import credentials
import time
from news import headlines

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

    for headline in headlines:
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


def twitter_search_users(retweeted_headlines):
    users_by_headline = []

    for headline, results in retweeted_headlines.items():
        user = {}
        for tweet in results['statuses']:
            user.update({'screen_name': tweet['user']['screen_name'],
                         'id': tweet['user']['id'],
                         'urls': tweet['entities']['urls'],
                         'verified': tweet['user']['verified'],
                         'protected': tweet['user']['protected'],
                         'created_at': tweet['user']['created_at'],
                         'statuses_count': tweet['user']['statuses_count'],
                         'description': tweet['user']['description']})
        if len(user.keys()) > 0:
            users_by_headline.append(user)
    return users_by_headline


def run_twitter_query():
    retweeted_headlines = twitter_search_headline()
    return twitter_search_users(retweeted_headlines)


def get_tweets_for_user(start_date, end_date, user_id, count):
    return api.GetUserTimeline(user_id=user_id, count=count)


def get_user(user_id, count):
    return api.GetUserTimeline(user_id=user_id, count=count)

# run_twitter_query()
