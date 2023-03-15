import pandas as pd

# Create a series
s = pd.Series([10,20,30,40,50])
s

df = pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_2/airlines.csv')
df.head()

#Extract a column and an individual column in a series in Pandas
carrier_column = df['carrier']

carrier_column
df['carrier']

s.index
s[3]

# Modify index from int to letters

s.index = ['a','b','c','d','e']
s

# Find value 40 

s['d']

first_row = df.loc[0]

first_row['name']


df
df.reset_index()
df.head()