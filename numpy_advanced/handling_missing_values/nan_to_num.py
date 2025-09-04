import numpy as np

arr = np.array([1,2,np.nan,4])

print(np.nan_to_num(arr,nan=3))