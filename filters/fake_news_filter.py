from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import urllib.request
import time
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.twitter_api import get_tweets_with_links

keywords = ["cookie", "copyright policy", "Data Policy", "Subscriber Agreement", "Your Ad Choices", "Site Feedback", "Advertising",
            "Guidelines", "Terms of Use", "Privacy Policy", "Accessibility Help", "Parental Guidance", "Get Personalised Newsletters"]
only_links = SoupStrainer("a")


def find_links(user):
    links = []
    if user['urls']:
        url = user['urls'][0]['expanded_url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser",
                             parse_only=only_links)
        for link in soup.find_all('a'):
            links.append(
                {
                    'text': link.string,
                    'link': link.get('href')
                }
            )
    return links


def probability_of_fake(keywords, links):
    # probability = 0
    lower_words = []
    for keyword in keywords:
        lower_words.append(keyword.lower())
    for link in links:
        if link['text'] in lower_words:
            return True


#def get_tweets_with_links():
#    api = twitterapi.api
#    return api.GetSearch(term="cyberpunk", count=5, return_json=True)


def fake_news_filter(user):
  pass

def output_users(results):
  pass

def scan_for_fake_news():
  results = get_tweets_with_links()
  users = output_users(results)

  for user in users:
    # page_links = find_links(user)
    print(probability_of_fake(links=[{'text': 'cookie'}], keywords=keywords))
