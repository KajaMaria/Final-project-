import math
from math import sqrt
import warnings
from collections import Counter
# import numpy as np

# Intruction:
# pip3 install numpy
# You can change value in the object. b is for bots potentially
# but not sure how are they going to look like on the graph?

# totalDistanceSquared=w0∗(V1[0]−V2[0])2+w1∗(V1[1]−V2[1])2+w2∗(V1[2]−V2[2])2+w3∗(V1[3]−V2[3])2+w4∗(V1[4]−V2[4])2
# 𝐷𝑖𝑠𝑡𝑥𝑦 = (
# 𝑚
# 𝑘=1 𝑥𝑖𝑘 − 𝑥𝑗𝑘 )
# 2


dataset = [3, 4, 5, 8, 11]
new_object = [2, 1, 4, 8, 10]


# def euclideanDistance(vector1, vector2, length):
#     distance = 0
#     for x in range(length):
#         distance += (vector1[x] - vector2[x]) ** 2
#     return math.sqrt(distance)


# print(euclideanDistance(dataset, new_object, 3))


def k_nearest_n(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to value smaller than deciding groups')
    distance = []
    vector1 = data
    vector2 = predict
    # range = len(data)
    single_vector_comparison = []
    for x in range(0, 5):
        single_vector_comparison.append(pow((vector1[x] - vector2[x]), 2))

    distance.append(single_vector_comparison)

    #     e_distance = (vector1[i] - vector2)**2
    #     print(e_distance)
    #     # e_distance = (data[0]- predict[0])**2 + (features[1]- predict[1])**2+ (features[2]- predict[2])**2 + (features[3]- predict[3])**2 + (features[4]- predict[4])**2
    #     # distances.append([e_distance, range])

    # votes = [i][1] for i in sorted(distances)[:k]]
    # # print(Counter(votes).most_common(1))
    # vote_result= Counter(votes).most_common(1)[0][0]

    # return vote_result


# result= k_nearest_n(dataset, new_object2)
# print(result)

# do we have two feature dinmention?
# dinamic number of features?
# how many neighbours so we have? more than 3?
# is it euclidean distance?
k_nearest_n(dataset, new_object, 5)
