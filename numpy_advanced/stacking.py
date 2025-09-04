"""


vertically ---> vstack() ---> works row wise
hstack ---> horizontally ---> works column wise


"""

import numpy as np

arr = ([1,2,3])
arr_n = ([4,5,6])
print(np.vstack((arr,arr_n))) #vertically stacking
print(np.hstack((arr,arr_n))) #horizontally stacking
