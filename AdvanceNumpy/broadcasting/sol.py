import numpy as np


original_prices = np.array([100,200,300,400])
discount = 10 #scalar single value
discounted_prices = original_prices - (original_prices * discount/100 )

print(discounted_prices)