from external_api.twitter_api import get_tweets_with_users
from external_api.news_api import get_headlines
from db.redis_cache import retrieve_headlines, store_headlines

headlines = get_headlines()
store_headlines(headlines)
headlines_thing = retrieve_headlines()
print(get_tweets_with_users(headlines_thing))

