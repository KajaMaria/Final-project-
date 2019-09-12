
from neo4j import GraphDatabase
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
import credentials
from db.redis_cache import retrieve_headlines, retrieve_users
from external_api.twitter_api import run_twitter_query

GRAPHENEDB_BOLT_USER = os.environ.get('GRAPHENEDB_BOLT_USER')
GRAPHENEDB_BOLT_PASSWORD = os.environ.get('GRAPHENEDB_BOLT_PASSWORD')
GRAPHENEDB_BOLT_URL = os.environ.get('GRAPHENEDB_BOLT_URL')

driver = GraphDatabase.driver(
    GRAPHENEDB_BOLT_URL, auth=(GRAPHENEDB_BOLT_USER, GRAPHENEDB_BOLT_PASSWORD))

## ---------------- ADDING USERS TO THE DB ----------------
# As we only have four methods by which a user should enter
# the project's database, i'm breaking those functions out
# below for easy reading.

def add_user_node_source_headline(user):
    source = user['source']
    with driver.session() as session:
        session.run("MERGE (a:User {screen_name: $user['screen_name'], id: $user['id'], created_at: $user['created_at'], followers_count: $user['followers_count'], statuses_count: $user['statuses_count']}) "#, score: $user['score'], average_tweets: $user['average_tweets'] status: $user['status']}) ",
                    "MERGE (s:Source {title: $source['title'], published_at: $source['published_at'], publisher: $source['publisher'], url: $source['url']}) "
                    "MERGE (a)-[:TWEETED]->(s) ",
                    user=user, source=source)

def add_user_node_source_text(user):
    source = user['source']
    with driver.session() as session:
        session.run("MERGE (a:User {screen_name: $user['screen_name'], id: $user['id'], created_at: $user['created_at'], followers_count: $user['followers_count'], statuses_count: $user['statuses_count']}) "#, score: $user['score'], average_tweets: $user['average_tweets'] status: $user['status']}) ",
                    "MERGE (s:Source {title: $source['title'], published_at: $source['published_at'], publisher: $source['publisher'], url: $source['url']}) "
                    "MERGE (a)-[:TWEETED]->(s) ",
                    user=user, source=source)

def add_user_node_source_hashtag(user):
    source = user['source']
    with driver.session() as session:
        session.run("MERGE (a:User {screen_name: $user['screen_name'], id: $user['id'], created_at: $user['created_at'], followers_count: $user['followers_count'], statuses_count: $user['statuses_count']}) "#, score: $user['score'], average_tweets: $user['average_tweets'] status: $user['status']}) ",
                    "MERGE (s:Source {title: $source['title'], published_at: $source['published_at'], publisher: $source['publisher'], url: $source['url']}) "
                    "MERGE (a)-[:TWEETED]->(s) ",
                    user=user, source=source)

def add_user_node_source_user(user):
    source = user['source']
    with driver.session() as session:
        session.run("MERGE (a:User {screen_name: $user['screen_name'], id: $user['id'], created_at: $user['created_at'], followers_count: $user['followers_count'], statuses_count: $user['statuses_count']}) "#, score: $user['score'], average_tweets: $user['average_tweets'] status: $user['status']}) ",
                    "MERGE (s:Source {title: $source['title'], published_at: $source['published_at'], publisher: $source['publisher'], url: $source['url']}) "
                    "MERGE (a)-[:TWEETED]->(s) ",
                    user=user, source=source)

## ---------------- ADDING RELATIONSHIPS TO THE DB ----------------
# These methods should be run in the event where in case there may
# be new unlinked bots to sources, or bots to other bots we can 
# update the db to reflect these relationships. I.e we can run the 
# following filter and see whether any of the following/followers 
# match a suspected bot in the database and then denote their
# relationship to each other.

def get_bots_and_following_relationships(first_user, second_user, bidirectional):
    # create a link between two nodes to denote that either one or 
    # both is following the other. Must be passed with the bidirectional
    # boolean - if false the first_user will be denoted as FOLLOWING the
    # second user, else they will be noted as following each other.
    # I have used first and second user here as it is clearer than following
    # and follower I believe, may be wrong here. 
    first_user_assignment = "MATCH (f:User {id: $first_user['id']})"
    second_user_assingment = "MATCH (s:User {id: $second_user['id']})"
    if bidirectional:
        build_relationships = "MATCH (f)<-[:FOLLOWING]->(s) RETURN u"
    else:
        build_relationships = "MATCH (f)-[:FOLLOWING]->(s) RETURN u"
    
    with driver.session() as session:
        session.run(first_user_assignment + 
                    second_user_assingment +
                    build_relationships, first_user=first_user, second_user=second_user
                    )
    

## ---------------- RETRIEVING DATA FROM THE DB ----------------
# These methods allow us to perform the necessescary operations to
# retrieve users, sources and stats from the db. 

def retrieve_all_data():
    # careful calling this, it can be a very large query / response
    # perhaps you actually need to retrieve only a single node or
    # cluster?
    with driver.session() as session:
        for record in session.run("MATCH (n) RETURN n "):
            return record

def retrieve_user(user):
    with driver.session() as session:
        for record in session.run("MATCH (u:User {id: $user['id']}) RETURN u", user=user):
            return record


# def retrieve_text_source(tx, text):
#     statement = "MATCH (a:Text { text: {text} }) RETURN a"
#     for record in tx.run(statement, text=text):
#         return record
        
# def retrieve_hashtag(tx, hashtag):
#     statement = "MATCH (a:Hashtag { text: {text} }) RETURN a"
#     for record in tx.run(statement, text=hashtag):
#         return record

# def get_oldest(tx):
#     statement = "MATCH (u:User) RETURN ORDER BY u.created_at DESC LIMIT 1"
#     pass

# def get_bots(tx):
#     records = tx.run("MATCH (u:User) RETURN u.screen_name as screen_name, u.id as id, u.created_at as created_at, u.followers_count as followers_count, u.statuses_count as statuses_count")#u.score as score, u.status as status, u.average_tweets as average_tweets")
#     users = []
#     for record in records:
#         user = {
#             "User": {
#                 "screen_name": record["screen_name"],
#                 "id": record["id"],
#                 "created_at": record["created_at"],
#                 "score": record["score"],
#                 "average_tweets": record["average_tweets"],
#                 "followers_count": record["followers_count"],
#                 "statuses_count": record["statuses_count"]
#                 # "status": record["status"]
#             }
#         }
#         users.append(user)
#     return users
#         # for i in record.items()[0][1].items():
#         #     print(i[0], i[1])
#     # something = [i['n'].items() for i in records]
#     # for some in something:
#     #     print(some.value())
#     # for record in tx.run("MATCH (n) RETURN n"):
#     #     for i, j in iter(record['n']):
#     #         print(j)
        

# def store_data(tx, function_name, data):
#     function = {
#         'user': add_user_node,
#         'text': add_text_node,
#         'hashtag': add_hashtag_node,
#         'relationship': add_relationship_node
#     }
#     function[function_name](data)
#     # session.write_transaction(element['type'], element['data'])

#     # with driver.session() as session:
#     #    users = retrieve_users()
#     #    print(users)
#     #    for user in users:
#     #        print(user)
#     #        session.write_transaction(add_node_user, user['screen_name'])
#     #    session.read_transaction(print_nodes)

# def relationships_data(tx):
    
#     tx.run("MERGE (b)-[:TWEETED {created_at: $text_string.created_date}]->(t) ",)

# def template_function(labels_data, relationships_data):
#     return {
#         "labels": labels_data,
#         "relationships": relationships_data
#     }


users = retrieve_users()

for user in users:
    add_user_node_source_headline(user=user)


# print(session.read_transaction(print_nodes))