# with ndim we can check number of dimenions in an array
import numpy as np
arr = [1,2,3,4],[5,6,7,8]

def get_ndin(arr):
    nndu = np.array(arr)
    return(np.ndim(nndu))


print(get_ndin(arr))