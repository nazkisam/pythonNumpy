import numpy as np

arr = np.array([1,2,np.nan])

cleaned_arr =np.nan_to_num(arr)

print(cleaned_arr)

print(np.isnan(cleaned_arr))