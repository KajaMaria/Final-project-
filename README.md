
# PRY

Tracking Twitter bots

### Installation:

Create a credentials.py file in main folder and add credentials for Twitter API and Newsapi:
```
os.environ['NEWS_KEY'] = ''
os.environ['CONSUMER_KEY'] = ''
os.environ['CONSUMER_SECRET'] = ''
os.environ['ACCESS_TOKEN_KEY'] = ''
os.environ['ACCESS_TOKEN_SECRET'] = ''
```

Install the modules:

```
pip3 install python-twitter newsapi
```

#pry
https://www.instagram.com/pry_final_project/

how to install this application for developmet: - create a credentials.py and use the secure credentials we provide - pip3 install python-twitter (installs twitter api dependency) - pip3 install newsapi (install newsheadline dependency)



print(date2)



For Heroku Scheduler: apsschedule==3.0.0 in requirements.txt


Tweets/Age - 240 a day 
statuses: "user": { "created_at": "Tue Jan 05 10:15:29 +0000 2010",

created_at	String	
The UTC datetime that the user account was created on Twitter. Example:

"created_at": "Mon Nov 29 21:18:15 +0000 2010"
datetime: 2019-09-04 14:06:31.520001

Datetimes may be specified in any timezone in a POST or PUT command using the ISO 8601 standard format for timezone. For example, 2017-07-10T08:00:00-0800 is an acceptable input value and will be automatically translated to the UTC value of 2017-07-10T16:00:00Z.

When using the analytics endpoints with granularity of DAY or TOTAL, the start_time value must be specified at midnight of the desired day in the local timezone of the account holder. The timezone offset to be used will be the offset of the current day, not the offset of the day in question. For example, for an ads account in America/Los_Angeles during Pacific Daylight Savings time, the UTC offset is -0700. Thus, in an analytics request, the time should be specified as: start_time=2017-05-21T07:00:00Z or start_time=2017-05-21T00:00:00-0700. If the ads account was in Asia/Tokyo, where the offset is always +09:00, the values would be specified as: start_time=2017-05-20T15:00:00Z or start_time=2017-05-21T00:00:00+0900.


Supported: Z, -HHMM, +HHMM, -HH:MM, +HH:MM, -HH, +HH

User: statuses_count": 3658


