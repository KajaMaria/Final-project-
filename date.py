from newsapi.newsapi_client import NewsApiClient
import os
import twitter
import credentials
import json
import time
import datetime

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

# print(article_title)

results = {}


for k, v in article_title.items():
    results[k] = api.GetSearch(raw_query="q={k}&count=100", return_json=True)

# with open("results_page1.json", "w") as file:
#     file.write(json.dumps(results))


# def return_users_with_created_at(results):
    for k, v in results.items():
        create_time = []
        for tweet in v['statuses']:
            create_time.append(tweet['user']['created_at'])
    # print(create_time)

for k, v in results.items():
    tweets = []
    for tweet in v['statuses']:
        tweets.append(tweet['user']['statuses_count'])
# print(tweets)



date_time_str = "Mon Nov 29 21:18:15 +0000 2010"
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

array_date = date_time_str.split(" ")
del array_date[0]
del array_date[3]
string = ' '
list_date = string.join(array_date)
date_object = datetime.datetime.strptime(list_date, '%b %d %H:%M:%S %Y').date()
date = datetime.datetime.now().date()
date2 = date - date_object
date3 = str(date2).split(" ")[0]
print(date3)

# date3 = datetime.datetime.strptime(created_time,"%a %b %d %H:%M:%S +0000 %Y").date()
