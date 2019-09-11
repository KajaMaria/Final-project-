from random import randint, randrange, uniform
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))    
#from db.redis_cache import store_mock_data_set
from db.postgresql_storage import create_classified_set_entry

def create_random_sample():
  vector = [0] * 6

  for i in [0,3]:
    vector[i] = uniform(0,1)

  for i in [1,2,4,5]:
    vector[i] = randint(0,1)

  return vector

DEFAULT_SET_SIZE = 200

def create_test_set(size=DEFAULT_SET_SIZE):
  mock_data = []
  for i in range(size):
    vector = create_random_sample()
    mock_data.append((vector, randint(0,1)))
  create_classified_set_entry(mock_data)

#create_test_set()
