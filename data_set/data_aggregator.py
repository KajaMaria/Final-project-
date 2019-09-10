import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
import json
import subprocess
from external_api.news_api import get_headlines
from external_api.twitter_api import twitter_search_tweets_by_headlines, twitter_search_users_by_tweets
from filters.verified_filter import unverified_and_unprotected_user_filter



# -------------------------------------------------------
#           utility functions
# -------------------------------------------------------


def collect_existing_users():
    classified_users = []
    with open('data_set.json', 'r') as file:
        for line in file:
            if line != '\n':
                classified_users.append(json.loads(line)['screen_name'])
    return classified_users


def append_classified_to_data_set():
    with open('new_data_set.json', 'r') as r_file:
        with open('data_set.json', 'a') as a_file:
            for line in r_file:
                a_file.write(line)

# --------------------------------------------------------


RETURNED_TWEETS_COUNT = 200


def query_for_users():
    headlines = get_headlines()
    tweets = twitter_search_tweets_by_headlines(
        headlines, RETURNED_TWEETS_COUNT)
    users = twitter_search_users_by_tweets(tweets)
    return [user for user in users if unverified_and_unprotected_user_filter(user)]


def prep_users_for_classification(users):
    user_names = [user['screen_name'] for user in users]
    unique_users = set(collect_existing_users())
    return [user for user in users if user['screen_name'] not in list(unique_users)]


def prep_classification_file(users):
    append_classified_to_data_set()

    with open('new_data_set.json', 'w') as file:
        for user in users:
            user_details = json.dumps({'id': user['id'],
                                       'screen_name': user['screen_name'],
                                       'url': 'https://twitter.com/{}'.format(user['screen_name']),
                                       'classification': ''})
            file.write(user_details+'\n')


def open_tabs_in_browser():
    with open('new_data_set.json', 'r') as file:
        for line in file:
            user = json.loads(line)
            subprocess.run(['open', '-a', 'Firefox', user['url']])


def classification_session():
    users = query_for_users()
    users = prep_users_for_classification(users)
    prep_classification_file(users)
    open_tabs_in_browser()

    # classify_data_set()


classification_session()
