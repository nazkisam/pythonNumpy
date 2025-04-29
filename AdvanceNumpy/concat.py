#if you want to join two arrays then we use the concatination function
import numpy as np

arr1 = np.array([1,2,3,5])
arr2 = np.array([6,7,8,9])

arrayConcat = np.concat((arr1,arr2)) 
print(arrayConcat)