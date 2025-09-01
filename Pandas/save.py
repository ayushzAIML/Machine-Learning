import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam'],
    "Age": [25,30,35],
    "City": ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df)

# df.to_csv('output.csv', index=False)  
# df.to_excel('output.xlsx', index=False)
# df.to_json('output.json', orient='records', lines=True)  # Save as JSON


