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

article_title = []

for article in top_headlines['articles']:
    article_title.append(article['title'])

article_title = list(set(article_title))
results = {}


for headline in article_title:
    results[headline] = api.GetSearch(term=headline, return_json=True)

# with open("results_page1.json", "w") as file:
#     file.write(json.dumps(results))
output = {}

for k, v in results.items():
    users = []
    for i in v['statuses']:
        users.append(i['user']['screen_name'])
    output[k] = users
    # print(output)



users_by_headline = []
for k, v in results.items():
    user_info = {}
    for tweets in v['statuses']:
        for tweet in tweets:
            user_info.update({'screen_name': tweets['user']['screen_name'],
                              'created_at': tweets['user']['created_at'],
                              'tweet_count': tweets['user']['statuses_count']})
    users_by_headline.append(user_info)
print(users_by_headline)

date_time_str = "Mon Nov 29 21:18:15 +0000 2010"
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

array_date = date_time_str.split(" ")
del array_date[0]
del array_date[3]
# string = ' '
list_date = ' '.join(array_date)
date_object = datetime.datetime.strptime(list_date, '%b %d %H:%M:%S %Y').date()
date = datetime.datetime.now().date()
date2 = date - date_object
date3 = int(str(date2).split(" ")[0])
# print(date3)

# date3 = datetime.datetime.strptime(created_time,"%a %b %d %H:%M:%S +0000 %Y").date()
