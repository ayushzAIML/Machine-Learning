import numpy as np

arr = np.array([1,2,np.inf,4])
print(np.isinf(arr))

# replacing the infinite number

rep_inf = np.nan_to_num(arr, posinf=1000)
print(rep_inf)