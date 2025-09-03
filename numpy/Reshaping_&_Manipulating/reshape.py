"""
reshape(rows,columns)specify new shape
if dimensions match only then reshape is possible
---reshaping doesn't create copy , it returns a view
"""


import numpy as np

arr = np.array([10,20,30,40,50,60,20,20])

reshaped_arr = arr.reshape(4,2)
print(reshaped_arr)