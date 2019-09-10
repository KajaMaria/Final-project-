import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from knn_classifer import knn_classifier
from filters.average_tweets_per_day_filter import average_tweets_per_day_filter
from filters.verified_filter import unverified_and_unprotected_user_filter
from filters.bot_bio_filter import bot_bio_filter
from filters.fake_news_filter import fake_news_filter
from filters.active_hours_per_day_filter import active_hours_per_day_filter
from filters.timeline_hashtags_filter import timeline_hashtags_filter
from filters.retweet_count_filter import retweet_ratio_filter
from filters.scan_user_following_followers_filter import bot_following_ratio_filter, bot_followers_ratio_filter

def run_filters_on_user(user,filters):
  if unverified_and_unprotected_user_filter(user):
    return 'Account is either verified or protected. Not a bot.'
  
  filter_function = {  
      'tweets_per_day_ratio': average_tweets_per_day_filter,
      'bot_bio': bot_bio_filter,
      'fake_news': fake_news_filter,
      'hours_per_day': active_hours_per_day_filter,
      'timeline_hashtags': timeline_hashtags_filter,
      'retweets_ratio': retweet_ratio_filter,
      'bot_following': bot_following_ratio_filter,
      'bot_follower': bot_followers_ratio_filter_
  }

  results = {}
  for filter_name in filters:
    results[filter_name] = function[filter_name](user)
  
  return results

def normalize_features(filters_scores_dict):
  # Normalize: upper limit for tweeting is one tweet per minute; divide the returned average per day by max tweets per day
  filters_scores_dict['tweets_per_day_ratio'] /= 60 * 24;
  # Normalize: turn eny boolean res into an integer value
  for filter_name, res in filters_score_dict:
    if type(res) == bool:
      filters_scores_dict[filter_name] = int(res)
  # Normalize: divide active hour by total hours in a day
  filters_scores_dict['hours_per_day'] /= 24


def run_knn_classifier(filters_score_vector):
  feature_vector = normalize_features(filters_score_vector)
  return knn_classifier(feature_vector)

def classify_user(user, filters):
  filters_scores = run_filters_on_user(user,filters)
  classification = run_knn_classifier(filter_scores.vlaues())
  return classification

