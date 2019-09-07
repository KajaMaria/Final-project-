from twitterapi import get_user


def timeline_characteristics():

    account_timeline = get_user(117019813784104140, 200)

    for tweet in account_timeline:
        text = tweet['text']
        print(text)


# identify repeating hashtags /
# 3-5 keywords in tweets to suggest bot's tendencies.


# def bot_characteristics(screenname, 200):

# for tweet in account_timeline:

#     tweet = ''.join(user['description'].split(' ')).lower()

#     bio.count(brexit)


# def bio_bot():
#     results = run_twitter_query()

#     for user in results:

#         bot = ['iamabot', 'imabot', 'justabot']
#         # description has whitespace removed and downcased
#         bot_bio = ''.join(user['description'].split()).lower()

#         if any(x in bot_bio for x in bot):
#             print("Bot")
#         else:
#             print("Not bot")


timeline_characteristics()
