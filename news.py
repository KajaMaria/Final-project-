from newsapi.newsapi_client import NewsApiClient
import os
import credentials
import json
import time


API_KEY = os.environ.get('NEWS_KEY')

# Innit
newsapi = NewsApiClient(api_key=(API_KEY))

# /v2/top-headlines
top_headlines = newsapi.get_everything(sources='reuters',
                                       domains='uk.reuters.com/news/',
                                       language='en')


article_title = []

for article in top_headlines['articles']:
    article_title.append(article['title'])

article_title = list(set(article_title))
