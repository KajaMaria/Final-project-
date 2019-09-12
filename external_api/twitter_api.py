import twitter
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
import credentials
from db.redis_cache import store_users, retrieve_headlines

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

DEFAULT_RETURNED_TWEETS = 100


def twitter_search_tweets_by_headlines(headlines=retrieve_headlines(), count=DEFAULT_RETURNED_TWEETS):
    results = []
    for headline in headlines:
        query_result = api.GetSearch(
            term=headline['title'], count=count, return_json=True)
        results.append({'source': headline, 'results': query_result})
    return results


def get_users_from_tweets(source_and_tweets):
      # creating a list of user dicts with a source key
    users_with_source = []
    for source_with_results in source_and_tweets:
        for tweet in source_with_results['results']['statuses']:
            user = ({'source': source_with_results['source'],
                     'source_type': 'news-headline',
                     'screen_name': tweet['user']['screen_name'],
                     'id': tweet['user']['id'],
                     'urls': tweet['entities']['urls'],
                     'verified': tweet['user']['verified'],
                     'protected': tweet['user']['protected'],
                     'created_at': tweet['user']['created_at'],
                     'statuses_count': tweet['user']['statuses_count'],
                     'followers_count': tweet['user']['followers_count'],
                     'description': tweet['user']['description']})
            if len(user.keys()) > 0:
                users_with_source.append(user)
    return users_with_source


def run_twitter_query():
    tweets_from_headlines_queries = twitter_search_tweets_by_headlines()
    users = get_users_from_tweets(tweets_from_headlines_queries)
    store_users(users)
    return users


def get_tweets_for_user(user_id, count, start_date=0, end_date=0):
    return api.GetUserTimeline(user_id=user_id, count=count)


def get_user_following_list(user_id):
    return api.GetFriendIDs(user_id=user_id)


def get_user_followers_list(user_id):
    return api.GetFriendIDs(user_id=user_id)


def get_user(user_id):
    return api.GetUser(user_id=user_id, return_json=True)


# def get_tweets_with_users(headlines):
#     tweeted_headlines = twitter_search_tweets_by_headlines(headlines)
#     users = twitter_search_users_by_tweets(tweeted_headlines)
#     return users

run_twitter_query()
