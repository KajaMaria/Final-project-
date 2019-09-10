import operator

training_set = [([3, 4, 5, 8, 11],0), ([1, 2, 4, 3, 9],0), ([4, 4, 7, 3, 4],1), ([1, 4, 9, 8, 8],1), ([7, 5, 3, 8, 9],0)]
test_set = [[2, 1, 4, 8, 10],[2,3,4,1,6],[7,34,2,5,7],[2,5,6,7,3],[16,22,7,8,4],[9,3,6,10,3],[14,17,3,8,6]]


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
    distances.append((training_set[x], dist))
  distances.sort(key=operator.itemgetter(1))
  return distances[:k]

def get_classification(nearest_neighbours, k):
  classification_score = sum([neighbour[0][1] for neighbour in nearest_neighbours])
  return int(classification_score > k/2)

def knn_classifier(training_set,test_instance,k):
  nearest_neighbours = get_nearest_neighbours(training_set, test_instance,k)
  return get_classification(nearest_neighbours, k)

def classify_data_set(training_set, data_set, k):
  classified_data_set = []
  for vector in data_set:
    classification = knn_classifier(training_set,vector,k)
    classified_data_set.append((vector,classification))
  return classified_data_set


print(classify_data_set(training_set,test_set,3))

