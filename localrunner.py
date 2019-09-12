from external_api.news_api import get_headlines
from external_api.twitter_api import run_twitter_query
from db.redis_cache import retrieve_users
from db.graphdb import add_user_node_source_headline

def get_new_users_from_headlines_and_store_them():
    get_headlines()
    run_twitter_query()
    users = retrieve_users()
    for user in users:
        add_user_node_source_headline(user)

get_new_users_from_headlines_and_store_them()