# Write basic server to serve the API

def get_graph(graph_model_name): 
  # Get the graph to show on page. 
  # The model_name is the model of the graph we're showing: linked bots, dead bots etc. 
  pass

def get_bot_stats(count=10):
  # Show stats on page. Count is to enable showing a short list on front page.
  # Add another link for more extensive data. As much as we get around to.
  pass

def alter_search_criteria(criteria, show_graph):
  # Enabling users to search by user name, free text and hashtag (we don't have this search yet)
  # This should return data rather than graphical representation.
  # If show_graph=true, call get_graph instead
  pass

def choose_filters(filters_list):
  # PROBLEM: if we modify the filters choice we can no longer score the users with our algo, it's untrained for this combination
  # POSSIBLE SOLUTION: make this a dev option only, not on site.
  # Enable users to retrain their scoring algo on their own set of data and pick the filters they want.
  pass

def get_suspicious_news_sites_list():
  # Return the list, with some fun info connected to it:
  # the related bot account (possible with its info), time since creation (if possible), preview image of the site (possible?)
  # If we get a whois - the wehre the site is registered etc.
  pass

def get_node_details(node_id):
  # When pressing a node in a graph, get more details on it 
  pass

def retrain_classification_algorithm():
  pass

def use_different_classifier():
  # Enable devs to use their own classifier on the data
  # For us it just means to call on a different method
  pass
