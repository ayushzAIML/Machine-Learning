""" boolean masking ---
 it's also 10 times faster than loops in case of filtering"""


import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[arr>25])