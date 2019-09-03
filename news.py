from newsapi import NewsApiClient
import os
import twitter
import credentials
import json


API_KEY = os.environ.get('NEWS_KEY')

# Innit
newsapi = NewsApiClient(api_key=(API_KEY))

# /v2/top-headlines
top_headlines = newsapi.get_everything(sources='reuters',
                                       domains='uk.reuters.com/news/',
                                       language='en')


API_CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
API_CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
API_ACCESS_TOKEN_KEY = os.environ.get('ACCESS_TOKEN_KEY')
API_ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')


api = twitter.Api(consumer_key=(API_CONSUMER_KEY),
                  consumer_secret=(API_CONSUMER_SECRET),
                  access_token_key=(API_ACCESS_TOKEN_KEY),
                  access_token_secret=(API_ACCESS_TOKEN_SECRET),
                  sleep_on_rate_limit=True)

# with open("headlines", "w") as file:
article_title = {}

for article in top_headlines['articles']:
    # file.write("%s\n" % article['title'])
    title = article['title']
    publishedDate = article['publishedAt']
    article_title[title] = publishedDate

results = {}

for headline in article_title:
    # string_check = 'q={}'.format(headline)
    results[headline] = (api.GetSearch(
        raw_query="q={headline}", return_json=True))

with open("results_page1.json", "w") as file:
    file.write(json.dumps(results))
