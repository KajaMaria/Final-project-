from classifier import knn_classifier, normalize_features
from average_tweets_per_day_filter import average_tweets_per_day_filter
from verified_filter import unverified_and_unprotected_user_filter
from bot_bio_filter import bot_bio_filter
from fake_news_filter import fake_news_filter
from active_hours_per_day_filter import active_hours_per_day_filter
from timeline_hashtags_filter import timeline_hashtags_filter


def run_filters_on_user(user,filters):
  if unverified_and_unprotected_user_filter(user):
    return 'Account is either verified or protected. Not a bot.'
  
  filters = set_filters_order(filters)
  filter_function = {  
      'tweets_per_day_ratio': average_tweets_per_day_filter,
      'bot_bio': bot_bio_filter,
      'fake_news': fake_news_filter,
      'hours_per_day': active_hours_per_day_filter,
      'timeline_hashtags': timeline_hashtags_filter
  }

  results = {}
  for filter_name in filters:
    results[filter_name] = function[filter_name](user)
  
  return results

def run_knn_classifier(filters_score_vector):
  feature_vector = normalize_features(filters_score_vector)
  return knn_classifier(feature_vector)

def classify_user(user, filters):
  filters_scores = run_filters_on_user(user,filters)
  filters_score_vector = [filter_result for filter_name, filter_result in filters_scores]
  return run_knn_classifier(filters_score_vector)

