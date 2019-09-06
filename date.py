import datetime
from utility import convert_timestamp_to_datetime
# from redis_cache import retrieve_users

NO_OF_TWEETS_PER_DAY_THRESHOLD = 200

def average_tweets_per_day(user):
  created_at_date = convert_timestamp_to_datetime(user['created_at']).date()
  current_date = datetime.datetime.now().date()
  user_active_days_count = current_date - created_at_date
  return user['statuses_count'] / user_active_days_count.days

def filter_by_average_tweets_per_day(user):
  average = average_tweets_per_day(user)
  return average >= NO_OF_TWEETS_PER_DAY_THRESHOLD

#def test_filter():
#  users = retrieve_users()
#  
#  suspected_bots = {}
#  humans = {}
#  for user in users:
#    res = filter_by_average_tweets_per_day(user)
#    if res:
#      suspected_bots[user['id']] = res
#    else:
#      humans[user['id']] = res
#  return {'bots': suspected_bots,'humans': humans}
#
#print(test_filter())
