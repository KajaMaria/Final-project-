from db.redis_cache import retrieve_headlines
from external_api.twitterapi import twitter_search_tweets_by_headlines
#import sys
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))

headlines = retrieve_headlines()
print(headlines)

print(twitter_search_tweets_by_headlines(headlines))

