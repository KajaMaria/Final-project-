from neo4j import GraphDatabase
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
import credentials


GRAPHENEDB_BOLT_USER = os.environ.get('GRAPHENEDB_BOLT_USER')
GRAPHENEDB_BOLT_PASSWORD = os.environ.get('GRAPHENEDB_BOLT_PASSWORD')
GRAPHENEDB_BOLT_URL = os.environ.get('GRAPHENEDB_BOLT_URL') 

driver = GraphDatabase.driver(
  GRAPHENEDB_BOLT_URL,auth=(GRAPHENEDB_BOLT_USER ,GRAPHENEDB_BOLT_PASSWORD))

session=driver.session()

def add_user_node(tx, name):
    tx.run("MERGE (a:User {name: $name}) ",
           #    "MERGE (h:Headline {headline: $headline}) "
           #    "MERGE (a)-[:RETWEETED]->(h)",
           name=name)

def add_text_node(tx, args):
    pass

def add_hashtag_node(tx, args):
    pass

def add_relationship_node(tx, args):
    pass

def retrieve_data(tx, query_param, return_param):
    for record in tx.run("MATCH ({}) RETURN {}".format(query_param, return_param)):
        print(record)

def store_data(tx, function_name, data):
    function={
      'user': add_user_node,
      'text': add_text_node,
      'hashtag' : add_hashtag_node,
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
