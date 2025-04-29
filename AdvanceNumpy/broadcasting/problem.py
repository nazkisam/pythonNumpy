import numpy as np

prices = [100,200,300]
discount = 10 
discounted_prices = []


for price in prices:
  final_price = price - (price * discount / 100)
  discounted_prices.append(final_price)

print(discounted_prices)  