from db.graphdb import retrieve_user, session, retrieve_text_source, retrieve_hashtag
# Write basic server to serve the API

# --------------------------
# Server API
# --------------------------

# Front End


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
    # Only viable for deterministic KNN (non weighted)
    # Wrapper for KNN (choose vector positions)
    pass


def get_suspended_bots():
    # Runs a query on the graph db for suspended bots
    # Add state for inactive, i.e when a bot is not suspended but no longer active
    pass


def get_suspicious_news_sites_list():
    # Return the list, with some fun info connected to it:
    # the related bot account (possible with its info), time since creation (if possible), preview image of the site (possible?)
    # If we get a whois - the wehre the site is registered etc.
    # If possible screenshot a preview of the website and display as thumbnail
    pass


def get_user_node(user_id):
  # need to retrieve a specific user's details to be displayed, watch for a get
  # request passing only a user id to retrieve that users data.
    data = retrieve_user(tx=session, user_id=user_id)
    user = {
        "name": data.properties['name'],
        "id": data.properties['id'],
        "age": data.properties['age'],
        "score": data.properties['score'],
        "average_tweets": data.properties['average_tweets'],
        "followers": data.properties['followers'],
        "total_tweets": data.properties['total_tweets'],
        "status": data.properties['status']
    }
    return user
    # When pressing a node in a graph, get more details on it
    # details to include for user:
    # - url to site
    # - name
    # - id
    # - age
    # - score(probability)
    # - number of tweets per day
    # - number of followers
    # - total number of tweets
    # - status (i.e active/inactive)


def get_text_node(text):
    data = retrieve_text_source(tx=session, text=text)
    text_node = {
        "text": data.properties['text'],
        "source": data.properties['source'],
    }
    if text_node['source'] != "User entered":
        append_data = {
            "News Outlet": data.properties['news_source'],
            "Headline Published": data.properties['created'],
            "Story URL": data.properties['url'],
        }
        text_node.update(append_data)
    return text_node
    # details to include for text node:
    # - text (string queried)
    # - origin of search (i.e freetext/headline)
    # should have a t/false for headline property so that if it is a
    # headline we can provide the original source link, may need to
    # re-write the headlines storage to do so.


def get_hashtag_node(hashtag):
    data = retrieve_hashtag(tx=session, hashtag=hashtag)
    hashtag_node = {
        "text": data.properties['text'],
        "trending": data.properties['trending'],
        "created": data.properties['created_at']
    }
    return hashtag_node
    # details to include for hashtag node:
    # - text (hashtag)
    # - trending (true/false)
    # details for relationships:
    # - following (created date, bidirectional, nodes related to self)
    # - source (created date, initiator(user), [user, headline, hashtag])
    # what was the search we ran for this user.


# here we are dividing the functionality of the get_bot_stats into smaller functions
def get_oldest():
    # check by created date
    pass


def most_popular():
    # get for number of followers
    pass


def most_active():
    # get highest number of averaged tweets per day
    pass


def biggest_cluster():
    # tentative on results of algorithm
    pass


def get_bot_characteristics():
    # tentative - would get hashtags, keywords, tweeting interval patterns
    pass

# Dev API


def retrain_classification_algorithm():
    pass


def use_different_classifier():
    # Enable devs to use their own classifier on the data
    # For us it just means to call on a different method
    pass
