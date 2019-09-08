import math
from math import sqrt
import warnings
from collections import Counter
import numpy as np

# Intruction:
# pip3 install numpy 
# You can change value in the object. b is for bots potentially 
# but not sure how are they going to look like on the graph?

# totalDistanceSquared=w0∗(V1[0]−V2[0])2+w1∗(V1[1]−V2[1])2+w2∗(V1[2]−V2[2])2+w3∗(V1[3]−V2[3])2+w4∗(V1[4]−V2[4])2
# 𝐷𝑖𝑠𝑡𝑥𝑦 = (
# 𝑚
# 𝑘=1 𝑥𝑖𝑘 − 𝑥𝑗𝑘 )
# 2
 

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

result = k_nearest_n(dataset, new_object1, k=3)
print(result)

# do we have two feature dinmention?
# dinamic number of features?
# how many neighbours so we have? more than 3?
# is it euclidean distance?