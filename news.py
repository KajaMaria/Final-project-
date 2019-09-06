from newsapi.newsapi_client import NewsApiClient
import os
import credentials


API_KEY = os.environ.get('NEWS_KEY')

# Init
newsapi = NewsApiClient(api_key=(API_KEY))

# /v2/top-headlines
top_headlines = newsapi.get_everything(sources='reuters',
                                       domains='uk.reuters.com/news/',
                                       language='en')


headlines = []

for article in top_headlines['articles']:
    headlines.append(article['title'])

headlines = list(set(headlines))

#print(headlines)
