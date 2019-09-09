from bs4 import BeautifulSoup, SoupStrainer
import requests
import urllib.request
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from external_api.twitter_api import get_tweets_with_links
from db.postgresql_storage import create_news_site_entry


keywords = ["cookie", "copyright policy", "Data Policy", "Subscriber Agreement", "Your Ad Choices", "Site Feedback", "Advertising", "Careers",
            "Guidelines", "Terms of Use", "Privacy Policy", "Accessibility Help", "Parental Guidance", "Get Personalised Newsletters", "Risk Management Solutions"]

only_links = SoupStrainer("a")


def find_links(user):
    links = []
    if not user['urls']:
        return None
    else:
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


def get_suspicious_sites(keywords, site, user):
    safeword = 0
    for link in site['links']:
        for keyword in keywords:
            if link['text'].lower().strip() in keyword.lower():
                safeword += 1
    site.update({'safeword': safeword})
    if site['safeword'] < 2:
        entry = [user['screen_name'], user['id'], site['url']]
        create_news_site_entry(entry)
        return site


def get_sites_with_user_mentioned(site, user):
    links = site['links']
    screen_name = user['screen_name']

    for link in links:
        if screen_name in link['text']:
            entry = [user['screen_name'], user['id'], site['url']]
            create_news_site_entry(entry)
            return {'screen_name': screen_name, 'url': site['url']}


def filter_by_site_links(user):
    site = find_links(user)
    if get_sites_with_user_mentioned(site=site, user=user) != None:
        print('user failed first filter')
        return True
    else:
        if get_suspicious_sites(keywords=keywords, site=site, user=user) != None:
            print('user failed at second filter')
            return True
        else:
            return False
