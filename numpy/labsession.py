import pandas as pd
import numpy as np
# 1️ Create DataFrame with missing values
data = {
    'Name': ['Ram', 'Sita', 'Arjun', 'Meena', 'John'],
    'Age': [25, None, 30, 22, 28],
    'Salary': [50000, 60000, None, 45000, 70000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'City': ['Bangalore', 'Chennai', 'Bangalore', 'Mumbai', 'Bangalore']
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# 2 Detect missing values
print("\nMissing Values:")
print(df.isnull())
# 3 Replace missing values with 0
df_filled = df.fillna(0)
print("\nAfter Replacing Missing Values with 0:")
print(df_filled)
# 4️ Drop rows containing missing values
df_dropped = df.dropna()
print("\nAfter Dropping Rows with Missing Values:")
print(df_dropped)
# 5️ Sort by Age (Ascending)
sorted_age = df_filled.sort_values(by='Age', ascending=True)
print("\nSorted by Age (Ascending):")
print(sorted_age)
# 6️ Sort by Salary (Descending)
sorted_salary = df_filled.sort_values(by='Salary', ascending=False)
print("\nSorted by Salary (Descending):")
print(sorted_salary)
# 7️ Groupby Department - Average Salary
avg_salary = df_filled.groupby('Department')['Salary'].mean()
print("\nAverage Salary per Department:")
print(avg_salary)
# 8️ Total Salary per Department
total_salary = df_filled.groupby('Department')['Salary'].sum()
print("\nTotal Salary per Department:")
print(total_salary)
# 9 ️Filter employees where Age > 25 AND City = 'Bangalore'
filtered = df_filled[(df_filled['Age'] > 25) & (df_filled['City'] == 'Bangalore')]
print("\nEmployees Age > 25 AND City = Bangalore:")
print(filtered)
# 10️ Create Tax column (10% of Salary)
df_filled['Tax'] = df_filled['Salary'].apply(lambda x: x * 0.10)
print("\nDataFrame with Tax column:")
print(df_filled