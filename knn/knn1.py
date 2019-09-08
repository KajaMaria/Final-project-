import math
from math import sqrt
import warnings
from collections import Counter
import numpy as np

dataset = {'n':[[1,2],[2,3],[2,2]], 'b':[[6,7],[7,8],[7,7]]}
new_object = [4,5]

def k_nearest_n(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('K is set to value smaller than deciding groups')
    distances = []
    for group in data:
        for features in data[group]:
            e_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([e_distance, group])
    votes = [i[1] for i in sorted(distances)[:n]]

    for i in sorted(distances)[:n]:
        i[i]


#    return vote_result 