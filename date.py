import datetime
from utility import convert_timestamp_to_datetime
from twitterapi import run_twitter_query

def average_tweets_per_day(user):
  created_at_date = convert_timestamp_to_datetime(user['created_at']).date()
  current_date = datetime.datetime.now().date()
  user_active_days_count = current_date - created_at_date
  return user['statuses_count'] / user_active_days_count.days

def filter_by_average_tweets_per_day():
  suspected_bots = []
  users = run_twitter_query()
  for user in users:
    if average_tweets_per_day(user) >= 240:
      suspected_bots.append(user)
  return suspected_bots

filter_by_average_tweets_per_day()
