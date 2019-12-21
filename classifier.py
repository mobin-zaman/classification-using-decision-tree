import pandas as pd

column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca",
                "thal", "status"]

data = pd.read_csv("processed.cleveland.data", names=column_names)

print(data)

# changing the columns to proper datatype
data_type_needs_to_be_changed = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal', 'status']

for columns in data_type_needs_to_be_changed:
    data[columns] = data[columns].astype('category')

# changing the value of the status column in order to change the status in either or 1
# as 0 indicates there is no heart diseases and the other numbers indicates there is heart disease


data['status'] = data['status'].replace(to_replace=[2,3, 4], value=[1, 1, 1])

# print(data.isnull().sum()) this is needed to check for the missing values, there were none

