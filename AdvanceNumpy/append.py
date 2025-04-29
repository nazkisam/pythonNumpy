#if you want to append the array at the end of the array
# a new arry will be created and the original array remains the same.


import numpy as np

arr = np.array([1,3,4,6])
newArr = np.append(arr, [10,20,30])

print(newArr)

reversedArray = newArr[::-1]
print(reversedArray)
