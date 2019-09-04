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

# .pop(4).pop(0)
print(array_date)


# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)
# print(date_time_obj)


date = datetime.datetime.now()
date2 = date + datetime.timedelta(days=0, seconds=0, microseconds=0,
                                  milliseconds=0, minutes=+5, hours=0, weeks=0)
print(date)
print(date2)
