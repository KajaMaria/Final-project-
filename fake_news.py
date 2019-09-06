from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import urllib.request
import time
from twitterapi import run_twitter_query, twitter_search_users

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
        site = {'url': url}
        for link in soup.find_all('a'):
            if link.string:
                links.append(
                    {
                        'text': link.string,
                        'link': link.get('href')
                    }
                )
        site.update({
            'links': links 
        })
    return site

def number_of_safeword_links(keywords, site):
    keywords_hash = { keyword.lower() : 0 for keyword in keywords }
    for link in site['links']:
        safeword = 0
        if link['text'].lower() in keywords_hash.keys():
            safeword += 1
        site.update(
            {
                'safeword': safeword            
            }
        )
    return site

users = run_twitter_query()

for user in users:
    page_links = find_links(user)
    print(number_of_safeword_links(site=page_links, keywords=keywords))
