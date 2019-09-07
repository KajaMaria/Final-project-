from twitterapi import get_user


def bio_hashtags(user_id, count):
    results = get_user(user_id, count)

    hashtags = 0

    for tweet in results:
        text = ''.join(tweet.text.lower().split(' '))

        if (text.count('#')) >= 3:
            hashtags += 1

    if hashtags > 100:
        hashtag_filter = {'user_id': user_id, 'hashtags': hashtags,
                          'count': count, 'description': "Suspicious"}
        print(hashtag_filter)
    else:
        hashtag_filter = {'user_id': user_id, 'hashtags': hashtags,
                          'count': count, 'description': "Not suspicious"}
        print(hashtag_filter)


bio_hashtags(102479353, 200)
