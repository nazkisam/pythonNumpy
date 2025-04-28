import numpy as np
#if axis = 0 then the array will be inserted row wise
# if axis = 1 then the array will be inserted col wise
#if axis = None the the array will be inserted as flattened

arr = np.array([[1,2],[3,4]])
arr2 = np.insert(arr, 0,[9,0], axis = None)

print(arr2)