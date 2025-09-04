import numpy as np

arr = ([[1,2,3],
        [4,5,6]])

arr_del = np.delete(arr,0,axis=1)
print(arr_del)