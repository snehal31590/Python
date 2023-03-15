import pandas as pd

from completejourney_py import get_data

cj_data = get_data()
df = (
    cj_data['transactions']
    .merge(cj_data['products'], how='inner', on='product_id')
    .merge(cj_data['demographics'], how='inner', on='household_id')
)

df.head()

df['sales_value'].plot.hist()