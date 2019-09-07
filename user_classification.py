from classifier import classify_user, estimate_and_normalize_features
from average_tweets_per_day_filter import filter_by_average_tweets_per_day
from verified_filter import unverified_and_unprotected_user_filter
from bot_bio_filter import bot_bio_filter
from fake_news_filter import fake_news_filter
from active_hours_per_day_filter import active_hours_per_day_filter

def set_filters_order(filters):
  pass

def run_filters_on_user(user,filters):
  if unverified_and_unprotected_user_filter(user):
    return 'Account is either verified or protected. Not a bot.'
  
  filters = set_filters_order(filters)
  filter_function = {  
      'tweets_per_day_ratio': filter_by_average_tweets_per_day,
      'bot_bio': bot_bio_filter,
      'fake_news': fake_news_filter,
      'hours_per_day': active_hours_per_day_filter
  }

  results = {}
  for filter_name in filters:
    results[filter_name] = function[filter_name](user)
  
  return results

def get_classification_score(user_data_vector):
  feature_vector = estimate_and_normalize_features(user_data_vector)
  bot_score = classify_user(feature_vector)
  return bot_score

