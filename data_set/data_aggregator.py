import subprocess
import json
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.news_api import get_headlines
from external_api.twitter_api import twitter_search_tweets_by_headlines, twitter_search_users_by_tweets

def collect_existing_users():
  classified_users = []
  with open('data_set.json','r') as file:
    for line in file:
      if line != '\n':
        classified_users.append(json.loads(line)['screen_name'])
  return classified_users


def append_classified_to_data_set():
  with open('new_data_set.json','r') as r_file:
    with open('data_set.json','a') as a_file:
      for line in r_file:
        a_file.write(line)

def get_users_for_classification():
  headlines = get_headlines()
  tweets = twitter_search_tweets_by_headlines(headlines,200)
  users = twitter_search_users_by_tweets(tweets)
  user_names = [user['screen_name'] for user in users]
  unique_users = set(collect_existing_users())
  users = [user for user in users if user['screen_name'] not in list(unique_users)]

  append_classified_to_data_set()

  with open('new_data_set.json','w') as file:
    for user in users:
      s = json.dumps({'id':user['id'], 
        'screen_name':user['screen_name'], 
        'url':'https://twitter.com/{}'.format(user['screen_name']), 
        'classification': ''})
      file.write(s+'\n')


def classify_data_set():
  with open('new_data_set.json','r') as file:
    for line in file:
      user = json.loads(line)
      subprocess.run(['/usr/bin/firefox', '--new-tab', user['url']])

def classification_session():
  get_users_for_classification()
  classify_data_set()

classification_session()
