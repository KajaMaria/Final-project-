from newsapi.newsapi_client import NewsApiClient
import os
import twitter
import credentials
import json
import time
import datetime

date_time_str = "Mon Nov 29 21:18:15 +0000 2010"
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')  

array_date= date_time_str.split(" ")
del array_date[0]
del array_date[3]
string=' '
list_date = string.join(array_date)

date_object = datetime.datetime.strptime(list_date, '%b %d %H:%M:%S %Y')

print(date_object)

date = datetime.datetime.now()
date2 = date - date_object

print(date)
print(date2)
