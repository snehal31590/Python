import pandas as pd
planes_df_1 =  pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_3/planes.csv')
planes_df_1.head()

# Extract first 5 rows from the df

planes_df_1.loc[0:4]

# All manufacturers is equal to embraer

planes_df_1['manufacturer'] == 'EMBRAER'

# All elements where this condition is true

planes_df_1[planes_df_1['manufacturer'] == 'EMBRAER']

# Engines > 2

planes_df_1[planes_df_1['engines'] > 2]

planes_df_1['engines'] > 2

# count
sum(planes_df_1['engines'] > 2)

# combine diff conditions

condition_1 = planes_df_1['engines'] > 2
planes_df_1[condition_1]

condition_2 = planes_df_1['manufacturer'] == 'AIRBUS'
planes_df_1[condition_1 & condition_2]

planes_df_1[condition_1 | condition_2]



# Knowledge check

# Silicing - When we are explicitly selecting certain row of interests,  Filtering -- get those obs that meets some condition

planes_df_1.loc[planes_df_1['engines'] > 3]

planes_df_1.loc[condition_1 & condition_2]


# Subsetting rows and columns

# Select variables : year & engine and get rows : manufacturer = EMBRAER

subsetted_rows = planes_df_1[planes_df_1['manufacturer'] == 'EMBRAER']
subsetted_rows.head()

# Extract column of interest from the subsetted rows

subsetted_col = subsetted_rows[['year','engines']]

subsetted_col.head()


# create rows and cols . Alternate way for above steps

rows = planes_df_1['manufacturer'] == 'EMBRAER'
cols = ['year','engines']

planes_df_1.loc[rows,cols]

# Extract planes made by BOEING with seats and model variables and then combine

rows = planes_df_1['manufacturer'] == 'BOEING'
cols = ['seats' , 'model']
planes_df_1.loc[rows,cols]


