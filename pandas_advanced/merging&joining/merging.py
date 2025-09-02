import pandas as pd


customer_info = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'Customer_Name': ['Alice', 'Bob', 'Charlie'],
    'Email': ['alice@email.com', 'bob@email.com', 'charlie@email.com']
})

df_cu = pd.DataFrame(customer_info)

order_data = {
    
    'Customer_ID': [1,2,3],
    'Order_Amount': [250, 400, 150]
}

df_od = pd.DataFrame(order_data)



df_merge = pd.merge(df_cu,df_od,on = "Customer_ID",how="inner")
print(df_merge)