import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def store_headlines(headlines):
  return r.set('headlines', json.dumps(headlines))

def store_users(users):
  return r.set('users', json.dumps(users))

def retrieve_headlines():
  return json.loads(r.get('headlines').decode("utf-8"))

def retrieve_users():
  return json.loads(r.get('users').decode("utf-8"))
