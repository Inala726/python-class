import numpy as np

# purchases = np.array([10,20,30,200,300])

# mean_value = purchases.mean()

# print(mean_value)

# income_distribution = np.array([500, 600, 700, 800, 1000, 10000, 50000])

# mean_value = income_distribution.mean()

# # median_value = np.median(income_distribution)

# print(mean_value)

data = np.array([503,45,50,52,55,60,65,150,200])
sorted_data = data.sort()
avg_data = data.mean()
middle = np.median(data)


# print(f"Mean = {avg_data}\nMedian = {middle}")