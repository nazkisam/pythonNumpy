import numpy as np

array_2d = np.array([[1,2,3], [4,5,6]]) #2x3

vector = np.array([1,2]) #1x2
 
vector_reshape = vector.reshape(2,1)
print(vector_reshape)

print(array_2d + vector_reshape)