from twitterapi import run_twitter_query


def bio_bot():
    results = run_twitter_query()

    for user in results:

        bot = ['iamabot', 'imabot', 'justabot']
        # description has whitespace removed and downcased
        bot_bio = ''.join(user['description'].split()).lower()

        if any(x in bot_bio for x in bot):
            print("Bot")
        else:
            print("Not bot")


bio_bot()
