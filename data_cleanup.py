import pandas as pd

data = pd.read_csv('dataset.csv')

# data["Age"].fillna(data["Age"].median(), inplace=True)

print(data.isnull().sum())
# data.drop(["Ticket", "Name", "PassengerId"], axis=1, inplace=True)








