import numpy as np 

arr1 = np.array([1,2,4,5,6])
arr2 = np.array([6,7,8,9,10])

vstack =  np.vstack((arr1,arr2)) 
hstack = np.hstack((arr1,arr2))
print(hstack)
print(vstack)