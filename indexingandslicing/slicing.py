import numpy as np

arr = np.array([1,2,3,4,5,6,7])

arrslc = arr[0:-1]
print(arrslc)


print(arr[:4])
print(arr[5:])
print(arr[:])

#this method includes whole array but skips as per mentioned
print(arr[::3])
#this reverses the array
print(arr[::-1])



#fancy indexing
#selecting mutiple elements at once
print(arr[[0,2,6]])
