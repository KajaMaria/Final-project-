from neo4j import GraphDatabase
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
import credentials

GRAPHENEDB_BOLT_USER = os.environ.get('GRAPHENEDB_BOLT_USER')
GRAPHENEDB_BOLT_PASSWORD = os.environ.get('GRAPHENEDB_BOLT_PASSWORD')
GRAPHENEDB_BOLT_URL = os.environ.get('GRAPHENEDB_BOLT_URL') 

driver = GraphDatabase.driver(
  GRAPHENEDB_BOLT_URL,auth=(GRAPHENEDB_BOLT_USER ,GRAPHENEDB_BOLT_PASSWORD))

session = driver.session()

def add_user_node(tx, name):
    tx.run("MERGE (a:User {name: $name}) ",
           #    "MERGE (h:Headline {headline: $headline}) "
           #    "MERGE (a)-[:RETWEETED]->(h)",
           name=name)


def print_nodes(tx):
    for record in tx.run("MATCH (n) RETURN n"):
        print(record)

def create_node(data):
  for element in data:
    function = {
      'user': add_user_node,
      'headline': add_headline_node,
      'relationship': add_relationship_node
    }
    session.write_transaction(element['type'],element['data'])

  
      #with driver.session() as session:
      #    users = retrieve_users()
      #    print(users)
      #    for user in users:
      #        print(user)
      #        session.write_transaction(add_node_user, user['screen_name'])
      #    session.read_transaction(print_nodes)
