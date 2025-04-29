import numpy as np

twoDarr = np.array([
  [1,3,4,5],
  [7,8,9,10]
  ])

newArrTwoD = np.delete(twoDarr,0,axis = 0)
print(newArrTwoD)