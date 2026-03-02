#data frames is a 2-dimentional labeled data

import pandas as pd

#create dataframe from list of dictionaries

data = [
    {"Name":"Ram", "Age":24},
{"Name":"Ragav", "Age":43},
{"Name":"Ragu", "Age":32},
{"Name":"Rama", "Age":23},
]
df = pd.DataFrame(data)
print(df)

#create dataframe from dictionary of series
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])
df = pd.DataFrame({'A': s1, 'B':s2})
print(df)

#create Dataframe from Numpy Array

import numpy as np
arr=np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(arr, columns=["A", "B"])
print(df)

#create dataframe using CSV file
df = pd.DataFrame()
print(df)

#create empty dataframe
df = pd.DataFrame()
print(df)

#create data frame with custoom index
data = {
    'Name':["Ram", "Sam"],
    "Age":[45,25]

}

df = pd.DataFrame(data, index=["Emp1", "Emp2"])
print(df)