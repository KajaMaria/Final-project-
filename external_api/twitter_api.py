from db.redis_cache import store_users, retrieve_headlines
import credentials
import twitter
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))

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


def twitter_search_tweets_by_headlines(headlines, count=DEFAULT_RETURNED_TWEETS):
    results = {}
    for headline in headlines:
        results[headline] = api.GetSearch(
            term=headline['title'], count=count, return_json=True)
    return results


def twitter_search_users_by_tweets(tweeted_headlines):
    users_by_headline = []

    for headline, results in tweeted_headlines.items():
        user = {}
        for tweet in results['statuses']:
            print(tweet['user'])
            user.update({'screen_name': tweet['user']['screen_name'],
                         'id': tweet['user']['id'],
                         'urls': tweet['entities']['urls'],
                         'verified': tweet['user']['verified'],
                         'protected': tweet['user']['protected'],
                         'created_at': tweet['user']['created_at'],
                         'statuses_count': tweet['user']['statuses_count'],
                         'followers_count': tweet['user']['followers_count'],
                         'description': tweet['user']['description']})
        if len(user.keys()) > 0:
            users_by_headline.append(user)
    return users_by_headline

def twitter_search_users_by_headlines(tweeted_headlines):
    users_by_headline = []

    for headline, results in tweeted_headlines.items():
        user = {}
        for tweet in results['statuses']:
            print(tweet['user'])
            user.update({'screen_name': tweet['user']['screen_name'],
                         'id': tweet['user']['id'],
                         'urls': tweet['entities']['urls'],
                         'verified': tweet['user']['verified'],
                         'protected': tweet['user']['protected'],
                         'created_at': tweet['user']['created_at'],
                         'statuses_count': tweet['user']['statuses_count'],
                         'followers_count': tweet['user']['followers_count'],
                         'description': tweet['user']['description']})
        if len(user.keys()) > 0:
            users_by_headline.append((user, headline))
    return users_by_headline

def run_twitter_query(headlines):
  tweeted_headlines = twitter_search_tweets_by_headlines(headlines)
  users = twitter_search_users_by_tweets(tweeted_headlines)
  store_users(users)
  return users

def get_tweets_for_user(user_id, count, start_date=0, end_date=0):
    return api.GetUserTimeline(user_id=user_id, count=count)

def get_user_following_list(user_id):
  return api.GetFriendIDs(user_id=user_id)

def get_user_followers_list(user_id):
  return api.GetFriendIDs(user_id=user_id)

def get_user(user_id):
  return api.GetUser(user_id=user_id,return_json=True)

def get_tweets_with_users(headlines): 
  tweeted_headlines = twitter_search_tweets_by_headlines(headlines)
  users = twitter_search_users_by_tweets(tweeted_headlines)
  return users




