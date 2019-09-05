import json


def bio_bot(**results):

    for k, v in results.items():

        bot = ['iamabot', 'imabot', 'justabot']
        # description has whitespace removed and downcased
        bot_bio = ''.join(v['description'].split()).lower()

        if any(x in bot_bio for x in bot):
            print("Bot")
        else:
            print("Not bot")


bio_bot(**results)
