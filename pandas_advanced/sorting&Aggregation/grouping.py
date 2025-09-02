import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia'],
    'Age': [25, None, 28, 35, 22, 40, 27, 32, 29, 26],
    'Salary': [50000, None, 55000, 70000, 48000, 80000, 53000, 62000, 57000, 51000],
    'Performance_Score': [88, None, 85, 90, 87, 95, 84, 89, 91, 86],
    'Education': ['Bachelors', None, 'Bachelors', 'PhD', 'Bachelors', 'PhD', 'Masters', 'Bachelors', 'Masters', 'Bachelors'],
    'Bonus': [2000, None, 2500, 4000, 1800, 5000, 2300, 3200, 2700, 2100]
}

df = pd.DataFrame(data)

# grouped = df.groupby("Education").agg(
#     Average_Salary=("Salary", "mean"),
#     Total_Bonus=("Bonus", "sum"),
#     Count=("Name", "count")
# ).reset_index()

# print(grouped)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)