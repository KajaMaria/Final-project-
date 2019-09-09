#import os
#import sys
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
#from db.redis_cache import retrieve_users

def unverified_and_unprotected_user_filter(user):
  return user['verified'] == False and user['protected'] == False

#def test_filter():
#  users = retrieve_users()
#  unfiltered_users = []
#  filtered = []
#  for user in users:
#    if unverified_and_unprotected_user_filter(user):
#      unfiltered_users.append(user['id'])
#    else:
#      filtered.append(user['id'])
#  print(unfiltered_users, filtered)
#
#test_filter()
