import credentials
from neo4j import GraphDatabase
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))


GRAPHENEDB_BOLT_USER = os.environ.get('GRAPHENEDB_BOLT_USER')
GRAPHENEDB_BOLT_PASSWORD = os.environ.get('GRAPHENEDB_BOLT_PASSWORD')
GRAPHENEDB_BOLT_URL = os.environ.get('GRAPHENEDB_BOLT_URL')

driver = GraphDatabase.driver(
    GRAPHENEDB_BOLT_URL, auth=(GRAPHENEDB_BOLT_USER, GRAPHENEDB_BOLT_PASSWORD))

session = driver.session()


def add_user_node(tx, user, source):
    tx.run("MERGE (b:Bot {screen_name: $user.screen_name, id: $user.id, age: $user.created_at, score: $user.score, average_tweets: $user.average_tweets, followers: $user.followers, total_tweets: $user.total_tweets, status: $user.status}) "
           "MERGE (s:Source {source: $source.source, content: $source.content}) "
           "MERGE (b)-[:TWEETED {created_at: $text_string.created_date}]->(t) ",
           user=user, source=source)
    # tx.run("MERGE (a:User {name: $name}) ",
    #        #    "MERGE (h:Headline {headline: $headline}) "
    #        #    "MERGE (a)-[:RETWEETED]->(h)",
    #        name=name)


def add_text_node(tx, source):
    tx.run("MERGE (s:Source {source: $source.source, content: $source.content}) ",
           source=source)


def add_hashtag_node(tx, source):
    tx.run("MERGE (s:Source {source: $source.source, content: $source.content}) ",
           source=source)


def add_relationship_node(tx, args):
    pass


def retrieve_all_data(tx):
    statement = "MATCH (n) RETURN n "
    for record in tx.run(statement):
        return record

def retrieve_user(tx, user_id):
    statement = "MATCH (a:User { id: {user_id} }) RETURN a"
    for record in tx.run(statement, user_id=user_id):
        return record

def retrieve_text_source(tx, text):
    statement = "MATCH (a:Text { text: {text} }) RETURN a"
    for record in tx.run(statement, text=text):
        return record
        
def store_data(tx, function_name, data):
    function = {
        'user': add_user_node,
        'text': add_text_node,
        'hashtag': add_hashtag_node,
        'relationship': add_relationship_node
    }
    function[function_name](data)
    # session.write_transaction(element['type'], element['data'])

    # with driver.session() as session:
    #    users = retrieve_users()
    #    print(users)
    #    for user in users:
    #        print(user)
    #        session.write_transaction(add_node_user, user['screen_name'])
    #    session.read_transaction(print_nodes)

