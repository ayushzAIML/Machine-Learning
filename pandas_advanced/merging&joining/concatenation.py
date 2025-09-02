import pandas as pd

df_region_1 = pd.DataFrame({
    "customerID" : [1,2],
    "Name" : ["Gopa","Raju"]
})

df_region_2 = pd.DataFrame({
    "customerID" : [1,2],
    "Name" : ["Ayush","juice"]
})

# df_concat = pd.concat([df_region_1,df_region_2], ignore_index=False)
df_concat = pd.concat([df_region_1,df_region_2], axis=1, ignore_index=False)
print(df_concat)