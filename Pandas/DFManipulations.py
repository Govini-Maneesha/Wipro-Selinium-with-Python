'''

Creating data

Selecting data

Filtering data

Cleaning data

Transforming columns

Aggregating data

Merging datasets

Exporting results
'''
import numpy as np
#Creating data DFR using the dictionary
import pandas as pd
data = {
"Name": ["Ram", "Sam", "John", "Priya"],
"Age": [25, 30, 28, 22],
"Salary": [40000, 50000, 45000, 38000]
}

df= pd.DataFrame(data)
print(df)

#Selecting single data
print(df ["Age"])

#select multiple data or ccolumns
print(df [["Age", "Name"]])

#select rows using iloc or loc
print(df.loc[0:2]) # nth index
print(df.iloc[0:1]) # n-1 index

#filtering based on the conditions
df = pd.DataFrame(data)
print(df)

#employees with salary > 40000
filtered = df[df["Salary"]>40000]
print(filtered)

filtered = df[df["Salary"]<=40000]
print(filtered)

filtered = df[(df["Salary"]>40000) & (df["Age"]>25)]
print(filtered)

#adding or modifying the colums
data = {
"Name": ["Ram", "Sam", "John", "Priya"],
"Salary": [40000, 50000, 45000, 38000]
}
df= pd.DataFrame(data)
#add the bonus column
df["Bonus"] = df["Salary"]*0.10
print(df)

#modify the current column - increase the salary
df["Increment"]= df["Salary"] + 2000
print(df)

#sorting data ascending or decending
data = {
"Name": ["Ram", "Sam", "John", "Priya"],
"Age": [25, 30, 28, 22],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)

#sort the salary in ascending
sorterd_df = df.sort_values("Salary",ascending=False)
print(sorterd_df)

#handling missing value

data = {
"Name": ["Ram", "Sam", None],
"Age": [25, np.nan, 28],
}
df = pd.DataFrame(data)
print("missing values")
print(df.isnull())

#replace all missing values (NAN, None, NaT) in the Dataframe with 0
df_filled = df.fillna(0)
print(df_filled)

data = {
"Age": [25, 30, None, 22],
"Salary": [40000, 50000, None, 38000]
}
df_filled = df.fillna(0)
print(df_filled)
#drop missing rows
data = {
"Name": ["A", "B", "C"],
"Age": [25, None, 22],
"Salary": [40000, 50000, None]

}
df = pd.DataFrame(data)
print(df)
df = df.dropna()
print(df)

#groupBy and Agrregation

data = {
"City": ["Delhi", "Mumbai", "Delhi", "Chennai"],
"Salary": [40000, 50000, 45000, 38000]
}
df = pd.DataFrame(data)
#average salary per city
result = df.groupby("City")["Salary"].mean()
print(result)
#Multiple Aggregation
result = df.groupby("City")["Salary"].agg(["mean", "sum", "count"])
print(result)

#Merging DataFrames
df1 = pd.DataFrame({
    "ID": [1, 2],
    "Name": ["Ram", "Sam"]
})

df2 = pd.DataFrame({
    "ID": [1, 2],
    "Salary": [40000, 50000]
})

merged = pd.merge(df1, df2, on="ID", how ="inner")
print(merged)

#removing Duplicates
data = {
    "Name": ["Ram", "Sam", "Ram"],
    "Salary": [40000, 50000, 40000],
}
df = pd.DataFrame(data)
print("Before removing duplicates:")
print(df)
df = df.drop_duplicates()
print("After removing duplicates:")
print(df)