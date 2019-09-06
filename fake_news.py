from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import urllib.request
import time
import twitterapi

keywords = ["cookie", "copyright policy", "Data Policy", "Subscriber Agreement", "Your Ad Choices", "Site Feedback", "Advertising",
            "Guidelines", "Terms of Use", "Privacy Policy", "Accessibility Help", "Parental Guidance", "Get Personalised Newsletters"]
only_links = SoupStrainer("a")

def find_links(user):
    if user['urls']:
        url = user['urls'][0]['expanded_url']
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser",
                             parse_only=only_links)
        links = []
        for link in soup.find_all('a'):
            links.append(
                {
                    'text': link.string,
                    'link': link.get('href')
                }
            )
    return links

def probability_of_fake(keywords, links):
    probability = 0
    dictOfKeywords = { word.lower(): "" for word in keywords}
    for link in links:
        if link['text'].contains(keyword):
            probability += 1


def get_tweets_with_links():
    api = twitterapi.api
    return api.GetSearch(term="cyberpunk", count=5, return_json=True)


results = get_tweets_with_links()
users = twitterapi.output_users(results)

for user in users:
    links = find_links(user)
    probability_of_fake(links=links, keywords=keywords)