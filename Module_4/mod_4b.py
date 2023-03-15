import pandas as pd


x = pd.DataFrame({'id': [1, 2, 3], 'val_x': ['x1', 'x2', 'x3']})
y = pd.DataFrame({'id': [1, 2, 4], 'val_y': ['y1', 'y2', 'y4']})

x
y

from completejourney_py import get_data

# get_data() provides a dictionary of several DataFrames
cj_data = get_data()
cj_data.keys()

cj_data['transactions'].head()

x.columns.intersection(y.columns)

transactions = cj_data['transactions']
demographics = cj_data['demographics']

# This is to find the common key/column between both the tables
transactions.columns.intersection(demographics.columns)

# By default merge will perform an inner join.

x.merge(y)

# If  which column to join on nor the type of join isn't specified then it performs merge where it uses overlapping of columns names as the keys.
x.merge(y, how='inner', on='id')

x.merge(y, how='left', on='id')

x.merge(y, how='right', on='id')