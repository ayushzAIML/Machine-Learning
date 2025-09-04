"""

np.array(array_1,array_2,axis=0)
or
np.array(array_1,array_2,axis=1)

"""





import numpy as np

array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])

con_array_1 = np.concatenate((array_1,array_2), axis=0)

print(con_array_1)

