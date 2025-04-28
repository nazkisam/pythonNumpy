#Reshaping =  not modifying the data but changing the shape🤣
#need to enter the rows and cols to define the new shape
#it only returs a view and it never returns a copy.



import numpy as np

arr = np.array([1,2,3,4,5,6])

reshapedArr = arr.reshape(2,3)
print(reshapedArr)



