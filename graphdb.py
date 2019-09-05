from neo4j import GraphDatabase
# from bs4 import BeautifulSoup
import requests
import urllib.request
import time
from twitterapi import run_twitter_query
import news
import credentials
import json

driver = GraphDatabase.driver(
    "bolt://localhost:7687", auth=("neo4j", "dansbugs"))


def add_node_user(tx, name):
    tx.run("MERGE (a:User {name: $name}) ",
           #    "MERGE (h:Headline {headline: $headline}) "
           #    "MERGE (a)-[:RETWEETED]->(h)",
           name=name)


def print_nodes(tx):
    for record in tx.run("MATCH (n) RETURN n"):
        print(record)


with driver.session() as session:
    output = run_twitter_query()
    print(output)
    for user in output:
        print(user)
        session.write_transaction(add_node_user, user['screen_name'])
    session.read_transaction(print_nodes)
