import pandas as pd

# df = pd.read_csv('sales_data_sample.csv', encoding = 'latin1')
# df = pd.read_json('sample_Data.json')

# print(df.head(10))
# print(df.tail(10))
# print(df)
data = {
    "Name": ['Ram','Shyam','Ghanshyam'],
    "Age": [25,30,35],
    "City": ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
# print(df.shape)
# print(df.describe())
# print(df.info())
# print(df.count(axis='columns'))
# print(df.columns)
print(df.shape)