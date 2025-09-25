import pandas as pd


# # data = {
# #     "Name": ["John", "Korede", "Daniel"],
# #     "Age": [23, 25, 30],
# #     "City": ["Lagos", "Abuja", "Port Harcourt"]
# # }

# # df = pd.DataFrame(data) 
# # print(df)

# work = {
#     "Name": ["Mike", "David", "Daniel", "Korede", "Stephanie", "Frank"],
#     "StudyHours": [5, 3, 8, 2, 7, 4],
#     "SleepHours": [7, 6, 6, 5, 8, 7],
#     "Score": [80, 60, 92, 55, 88, 72]
# }
# df = pd.DataFrame(work)
# print(df)  
# print(df.info())
# print(df.describe())

# data = pd.read_csv("dataset.csv")
# print(data.head())
# print(data.tail())

data = pd.read_csv("data.csv")
# print(data.head())
# print(data.tail())
# print(data.info())
# print(data.describe())
# print(data.columns)
# print(data.shape) 
print(data["diagnosis"])
# print(data.plot())