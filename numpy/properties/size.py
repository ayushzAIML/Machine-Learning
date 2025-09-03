# will return total number of elements with numpy.size
import numpy as np
arr = [1,2,3,4,5],[1,2,3,4,5]
def get_size(arr):
    numpu = np.array(arr)
    return(np.size(numpu))

print(get_size(arr))