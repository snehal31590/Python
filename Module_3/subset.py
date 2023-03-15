import pandas as pd

planes_df =  pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_3/planes.csv')

planes_df

#Extract one column
planes_df['model']

#Verify type

type(planes_df['model'])

# To retain a column as DF
planes_df[['model']]

#Know the type
type(planes_df[['model']])

# What all columns are present
planes_df.columns


# Selecting is a common term for subsetting a DF
planes_df[['type','model']]

