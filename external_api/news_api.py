from newsapi.newsapi_client import NewsApiClient
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
from db.redis_cache import store_headlines, retrieve_headlines
import credentials

API_KEY = os.environ.get('NEWS_KEY')

# Init
newsapi = NewsApiClient(api_key=(API_KEY))

LANGUAGE = 'en'
COUNTRY = 'gb'

# /v2/top-headlines
def get_articles_from_newsapi(sources,domains,language):
  results = newsapi.get_everything(sources=','.join(sources),#'reuters',
                                       domains=','.join(domains),#'uk.reuters.com/news/',
                                       language=language)#'en')
  return results

def get_headlines(language=None, country=None):
  language = language or LANGUAGE
  sources, domains = set_sources_and_domains_for_newsapi(language, country or COUNTRY)
  newsapi_results = get_articles_from_newsapi(sources,domains,language)
  headlines = []
  
  for article in newsapi_results['articles']:
    headlines.append(article['title']) 
  headlines = (list(set(headlines)))
  store_headlines(headlines)
  return headlines


def get_sources(language=None, country=None):
  if country:
    return newsapi.get_sources(language=language or LANGUAGE,
                                country=country)
  else:
    return newsapi.get_sources(language=language)


def set_sources_and_domains_for_newsapi(language=None, country=None):
  newsapi_sources = get_sources(language, country)['sources']
  sources = []
  domains = []
  for source in newsapi_sources:
    sources.append(source['id'])
    domains.append(source['url'])
  return sources, domains

get_headlines()

