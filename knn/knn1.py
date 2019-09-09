import math
from math import sqrt
import warnings
from collections import Counter
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


dataset = [[3, 4, 5, 8, 11], [1, 2, 4, 3, 9], [
    4, 4, 7, 3, 4], [1, 4, 9, 8, 8], [7, 5, 3, 8, 9]]
new_object = [2, 1, 4, 8, 10]


vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]

def euclidean_distance(vector1, vector2, length):
    vector_length = len(vector1) 
    squared_distance = 0
    for i in range(vector_length):
        squared_distance += (vector1[i] - vector2[i])**2

    return squared_distance

def k_nearest_n(testSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(testSet)):
        dist = euclidean_distance(testInstance, testSet[x], length)
        print(dist)
        distances.append((testSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbor=[]
    for x in range(k):
        neighbor.append(distances[x][0])
    print(neighbor)

#     e_distance = (vector1[i] - vector2)**2
#     print(e_distance)
#     # e_distance = (data[0]- predict[0])**2 + (features[1]- predict[1])**2+ (features[2]- predict[2])**2 + (features[3]- predict[3])**2 + (features[4]- predict[4])**2
#     # distances.append([e_distance, range])

# votes = [i][1] for i in sorted(distances)[:k]]
# # print(Counter(votes).most_common(1))
# vote_result= Counter(votes).most_common(1)[0][0]
# print(vote_result)

# result= k_nearest_n(dataset, new_object2)
# print(result)

# euclidean_distance(vector1, vector2)
k_nearest_n(vector1,vector2,3)
