import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.twitter_api import get_tweets_for_user

BOT_RETWEET_LIMIT = 0.9
COUNT = 200 

def retweet_count(user_id, count=COUNT, bot_retweet_limit=BOT_RETWEET_LIMIT):
    
  tweets = get_tweets_for_user(user_id, count)  
  retweets = 0

  for tweet in tweets:
    if tweet.retweeted_status:
      retweets += 1
  
  retweets_ratio = retweets / count
  description = 'Suspicious' if retweets_ratio >= bot_retweet_limit else 'Not Suspicious'
  
  return {'user_id': user_id, 'bot_retweet_limit': bot_retweet_limit, 'count': retweets, 'description': description, 'retweets_ratio': retweets_ratio}

def retweet_ratio_filter(user_id,count=COUNT):
  return retweet_count(user_id,count)['retweets_ratio'] >= BOT_RETWEET_LIMIT

print(retweet_ratio_filter(331085505,50))
