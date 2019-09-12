import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from knn_classifier.knn_classifier import classify_vector
from filters.average_tweets_per_day_filter import average_tweets_per_day_filter
from filters.verified_filter import unverified_and_unprotected_user_filter
from filters.bot_bio_filter import bot_bio_filter
from filters.fake_news_filter import filter_by_site_links
from filters.active_hours_per_day_filter import active_hours_per_day_filter
from filters.timeline_hashtags_filter import timeline_hashtags_filter
from filters.retweet_count_filter import retweet_ratio_filter
from filters.scan_user_following_followers_filter import bot_following_ratio_filter, bot_followers_ratio_filter
from external_api.twitter_api import get_user
from db.postgresql_storage import create_classified_set_entry

def get_chosen_filters(filters):
  filter_function = {  
      'tweets_per_day_ratio': (average_tweets_per_day_filter,0),
      'bot_bio': (bot_bio_filter,1),
      'fake_news': (filter_by_site_links,2),
      'hours_per_day': (active_hours_per_day_filter,3),
      'timeline_hashtags': (timeline_hashtags_filter,4),
      'retweets_ratio': (retweet_ratio_filter,5),
      'bot_following': (bot_following_ratio_filter,6),
      'bot_follower': (bot_followers_ratio_filter,7)
  }
  f_tuples = [(f,filter_function[f]) for f in filters]
  f_tuples.sort(key= lambda t: t[1][1])
  return f_tuples

def get_training_set_id(filter_tuples):
  #filter_tuples = get_chosen_filters(filters)
  unique_filter_identifiers = [2,3,5,7,11,13,17,19]
  training_set_identifier = 1
  for f_tuple in filter_tuples:
    training_set_identifier *= unique_filter_identifiers[f_tuple[1][1]]
  return training_set_identifier

def run_filters_on_user(f_tuples,user):
  #  filter_function = {  
  #      'tweets_per_day_ratio': (average_tweets_per_day_filter,0),
  #      'bot_bio': (bot_bio_filter,1),
  #      'fake_news': (filter_by_site_links,2),
  #      'hours_per_day': (active_hours_per_day_filter,3),
  #      'timeline_hashtags': (timeline_hashtags_filter,4),
  #      'retweets_ratio': (retweet_ratio_filter,5),
  #      'bot_following': (bot_following_ratio_filter,6),
  #      'bot_follower': (bot_followers_ratio_filter,7)
  #  }
  #  
  #  f_tuples = [(f,filter_function[f]) for f in filters]
  #  f_tuples.sort(key= lambda t: t[1][1])
  results = []
     
  for f_tuple in f_tuples:
    filter_score = f_tuple[1][0](user)
    filter_score = normalize_feature(f_tuple[0], filter_score)
    results.append(filter_score)
  return results

def normalize_feature(f_name, score):
  # Normalize: upper limit for tweeting is one tweet per minute; divide the returned average per day by max tweets per day
  if f_name == 'tweets_per_day_ratio':
    return score / (60 * 24)
  # Normalize: divide active hours by total hours in day
  if f_name == 'hours_per_day':
    return score / 24
  # Normalize: turn any boolean res into an integer value
  if type(score) == bool:
    return int(score)
  return score

def run_knn_classifier(features_vector, training_set_identifier):
  return classify_vector(training_set_identifier,features_vector,3)

def classify_user(user, filters, training_set_id):
  if not unverified_and_unprotected_user_filter(user):
    return None

  filters_results = run_filters_on_user(filters,user)
  classification = run_knn_classifier(filters_results,str(training_set_id))
  return classification

def classify_users(users, filters):
  f_tuples = get_chosen_filters(filters)
  training_set_id = get_training_set_id(f_tuples)
 
  classified_users = [] 
  for user in users:
    classified_user = classify_user(user,f_tuples,training_set_id) 
    print(classified_user)
    if classified_user != None:
      classified_users.append(classified_user)
  print(classified_users)
  create_classified_set_entry(classified_users,training_set_id)
  return classified_users

#user = get_user(998852942223507457)
#print(classify_user(user,['tweets_per_day_ratio', 'bot_bio','hours_per_day','timeline_hashtags','retweets_ratio','fake_news']))
