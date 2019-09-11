import datetime
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from utility import convert_timestamp_to_datetime
from external_api.twitter_api import get_tweets_for_user 
#from db.redis_cache import retrieve_users

QUERY_TWEETS_COUNT_PER_USER = 200

def map_activity_hours(tweets_timestamps):
  activity_map = {}
  for timestamp in tweets_timestamps:
    created_at = convert_timestamp_to_datetime(timestamp)
    created_at_date = created_at.date()
    if created_at_date in activity_map:
      activity_map[created_at_date].add(created_at.hour)
    else:
      activity_map[created_at_date] = set([created_at.hour])
  return activity_map


  
def calculate_average_activity_hours_per_day(activity_dict):#tweets_timestamps):
  total_hours = 0
  for day,hours in activity_dict.items():
    total_hours += len(hours)
  active_days_count = len(activity_dict.keys())
  average_hours_per_day = total_hours / active_days_count
  return active_days_count, average_hours_per_day

def get_tweets_timestamp(tweets):
  timestamps = []
  for tweet in tweets:
    timestamps.append(tweet.created_at)
  return timestamps

def get_user_activity_hours_per_day(user_id,start_date, end_date):
  tweets = get_tweets_for_user(user_id,QUERY_TWEETS_COUNT_PER_USER,start_date,end_date)
  timestamps = get_tweets_timestamp(tweets)
  activity_dict = map_activity_hours(timestamps)
  return calculate_average_activity_hours_per_day(activity_dict)

def active_hours_per_day(user,start_date,end_date):
  total_number_of_days = (start_date - end_date)
  active_days_count, average_hours_per_day = get_user_activity_hours_per_day(user['id'],start_date,end_date)
  return {'user_id': user['id'], 'total_number_of_days': total_number_of_days, 'active_days_count': active_days_count, 'average_hours_per_day': average_hours_per_day}

def active_hours_per_day_filter(user,start_date=0,end_date=0):
  return active_hours_per_day(user,start_date,end_date)['average_hours_per_day']

#def test_filter():
#  users = retrieve_users()
#  print(active_hours_per_day_filter(users,0,0))

#test_filter()
