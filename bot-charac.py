from twitterapi import get_user


def timeline_characteristics():

    account_timeline = get_user(937962626222497793, 2)

    for tweet in account_timeline:

        print(tweet.text)


# identify repeating hashtags /
# 3-5 keywords in tweets to suggest bot's tendencies.

timeline_characteristics()
