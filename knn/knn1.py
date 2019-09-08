import math
from math import sqrt
import warnings
from collections import Counter
import numpy as np

# pip3 install numpy 

dataset = {'k':[[1,2],[2,3],[2,2]], 'b':[[6,7],[7,8],[7,7]]}
new_object = [1,1]
new_object1 = [3,5]
new_object1 = [7,8]

def k_nearest_n(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to value smaller than deciding groups')
    distances = []
    for group in data:
        for features in data[group]:
            e_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([e_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result =  Counter(votes).most_common(1)[0][0]

    return vote_result 

result = k_nearest_n(dataset, new_object, k=3)
print(result)

# do we have two feature dinmention?
# dinamic number of features?
# how many neighbours so we have? more than 3?
# is it euclidean distance?