import operator
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir))
#from db.redis_cache import retrieve_mock_data_set
from db.postgresql_storage import get_classified_set

#training_set = [([3, 4, 5, 8, 11],0), ([1, 2, 4, 3, 9],0), ([4, 4, 7, 3, 4],1), ([1, 4, 9, 8, 8],1), ([7, 5, 3, 8, 9],0)]
#test_set = [[2, 1, 4, 8, 10],[2,3,4,1,6],[7,34,2,5,7],[2,5,6,7,3],[16,22,7,8,4],[9,3,6,10,3],[14,17,3,8,6]]

#def get_classified_set_from_redis():
#  return retrieve_mock_data_set()    

def get_classified_set_from_db(): #From Postgres
  s = get_classified_set()
  print(s)
  return s

def euclidean_distance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return distance

def get_nearest_neighbours(classified_set, test_instance, k):
  distances = []
  length = len(test_instance)
  for x in range(len(classified_set)):
    dist = euclidean_distance(test_instance, classified_set[x][0], length)
    distances.append((classified_set[x], dist))
  distances.sort(key=operator.itemgetter(1))
  print(distances[:k])
  return distances[:k]

def get_classification(nearest_neighbours, k):
  classification_score = sum([neighbour[0][1] for neighbour in nearest_neighbours])
  return int(classification_score > k/2)

def knn_classifier(training_set,test_instance,k):
  nearest_neighbours = get_nearest_neighbours(training_set, test_instance,k)
  return get_classification(nearest_neighbours, k)

def classify_data_set(training_set, data_set, k):
  classified_data_set = []
  for element in data_set:
    classification = knn_classifier(training_set,element,k)
    classified_data_set.append((element,classification))
  return classified_data_set


#print(classify_data_set(get_classified_set_from_redis(),[[0.917009396, 1, 1, 0.6670261935, 1, 1]],3))
print(classify_data_set(get_classified_set_from_db(),[[0.917009396, 1, 1, 0.6670261935, 1, 1]],3))

