import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Helen', 'Ian', 'Julia'],
    'Age': [25, 30, 28, 35, 22, 40, 27, 32, 29, 26],
    'Salary': [50000, 60000, 55000, 70000, 48000, 80000, 53000, 62000, 57000, 51000],
    'Performance_Score': [88, 92, 85, 90, 87, 95, 84, 89, 91, 86],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Experience_Years': [2, 5, 3, 8, 1, 10, 4, 6, 3, 2],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'F'],
    'Location': ['NY', 'LA', 'NY', 'SF', 'LA', 'SF', 'NY', 'LA', 'SF', 'NY'],
    'Education': ['Bachelors', 'Masters', 'Bachelors', 'PhD', 'Bachelors', 'PhD', 'Masters', 'Bachelors', 'Masters', 'Bachelors'],
    'Bonus': [2000, 3000, 2500, 4000, 1800, 5000, 2300, 3200, 2700, 2100]
}

df = pd.DataFrame(data)

# print("Sample dataframe")
# print(df)

print("Name (single column return series)")
name = df["Name"]
print(name)


# selecting multiple columns
subset = df[["Name", "Salary"]]

print("\nSubset with Name and Salary")
print(subset)