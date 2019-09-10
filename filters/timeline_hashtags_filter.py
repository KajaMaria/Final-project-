import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.twitter_api import get_tweets_for_user

COUNT = 200
TWEETED_TAGS_THREASHOLD = 3
MARKED_TWEETS_THREASHOLD = 100

def get_timeline_hashtags_stats(user_id, count=None):
  count = count or COUNT
  tweets = get_tweets_for_user(user_id=user_id,count=count)

  hashtagged_tweets = 0

  for tweet in tweets:
    text = ''.join(tweet.text.lower().split(' '))

    if (text.count('#')) >= TWEETED_TAGS_THREASHOLD:
      hashtagged_tweets += 1
    
  return {'user_id': user_id, 
      'hashtags': hashtagged_tweets,
      'count': count, 
      'description': ("Suspicious" if hashtagged_tweets > MARKED_TWEETS_THREASHOLD else "Not suspicious"), 
      'ratio': hashtagged_tweets/count}

def timeline_hashtags_filter(user_id, count=None):
  return get_timeline_hashtags_stats(user_id, count)['ratio']

print(timeline_hashtags_filter(102479353))
