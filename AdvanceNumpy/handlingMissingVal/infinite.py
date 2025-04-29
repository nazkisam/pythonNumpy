import numpy as np
 
arr = np.array([1,2,np.inf,-np.inf,6])

print(np.isinf(arr))

#how to handle it

cleaned_arr = np.nan_to_num(arr,posinf = 1000 , neginf = 1000)

print(cleaned_arr)

print(np.isinf(cleaned_arr))