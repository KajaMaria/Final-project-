from twitterapi import get_user


def retweet_count(user_id, count, bot_retweet_limit=180):
    results = get_user(user_id, count)

    retweets = 0

    for tweet in results:

        if tweet.id != user_id:
            retweets += 1

    if retweets >= bot_retweet_limit:
        retweet_timeline_count = {
            'user_id': user_id, 'bot_retweet_limit': bot_retweet_limit, 'count': retweets, 'description': "Suspicious"}
        print(retweet_timeline_count)
    else:
        retweet_timeline_count = {'user_id': user_id, 'bot_retweet_limit': bot_retweet_limit,
                                  'count': retweets, 'description': "Not Suspicious"}
        print(retweet_timeline_count)


retweet_count()
