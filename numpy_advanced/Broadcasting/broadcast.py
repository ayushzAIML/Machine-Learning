# prices = [100,200,300]
# discount = 10

# final_price =[]

# for price in prices:
#     final_prices = price - (price * 10/100)
#     final_price.append(final_prices)

# print(final_price)





# now let's do this in numpy way

import numpy as np

prices = np.array([100,200,300])
discount = 10

final_prices = prices-(prices*discount/100)

print(final_prices)
