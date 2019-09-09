import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.twitter_api import get_tweets_for_user


def timeline_characteristics():

    account_timeline = get_tweets_for_user(937962626222497793, 2)

    for tweet in account_timeline:

        print(tweet.text)


# identify repeating hashtags /
# 3-5 keywords in tweets to suggest bot's tendencies.

timeline_characteristics()

