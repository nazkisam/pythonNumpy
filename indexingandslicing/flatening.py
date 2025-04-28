#when we want to convert multidimentionl array into a one d array

#.ravel - returs a view
#flatten -> returns a copy.

import numpy as np

arr = np.array([
  [2,3,4,5,6],
  [4,5,6,7,8]
])

print(arr.ravel())
print(arr.flatten())

print(arr)