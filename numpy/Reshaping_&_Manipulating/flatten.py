""".ravel() ---> returns views---> original data is effected
.flatten() ---> returns copy---> original data isn't effected"""

import numpy as np

arr_2D = np.array([[10,20,30],[40,50,60]])

print(arr_2D.ravel())
print(arr_2D.flatten())

