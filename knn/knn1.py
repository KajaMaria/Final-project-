import math
from math import sqrt
import warnings
from collections import Counter
import operator
import random
import math
import operator

# Intruction:
# pip3 install numpy
# You can change value in the object. b is for bots potentially
# but not sure how are they going to look like on the graph?

# totalDistanceSquared=w0∗(V1[0]−V2[0])2+w1∗(V1[1]−V2[1])2+w2∗(V1[2]−V2[2])2+w3∗(V1[3]−V2[3])2+w4∗(V1[4]−V2[4])2
# 𝐷𝑖𝑠𝑡𝑥𝑦 = (
# 𝑚
# 𝑘=1 𝑥𝑖𝑘 − 𝑥𝑗𝑘 )
# 2


trainingSet = [[3, 4, 5, 8, 11], [1, 2, 4, 3, 9], [
    4, 4, 7, 3, 4], [1, 4, 9, 8, 8], [7, 5, 3, 8, 9]]
testInstance = [2, 1, 4, 8, 10]


vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]

 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 
print(getNeighbors(trainingSet, testInstance,3))