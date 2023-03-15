import pandas as pd


# Import a data frame
df = pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_2/airlines.csv')
df.head()

#Extract a column and an individual column in a series in Pandas
carrier_column = df['carrier']

carrier_column

# Above is series which is always 1D,

carrier_column.shape

# A data frame has 2 Dimensions

df.shape
carrier_column.to_list()

df.head(1)

#Pull out / fetch 1st row

first_row = df.loc[0]
first_row

type(first_row)




