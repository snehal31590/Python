import pandas as pd

ames_1 = pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_3/ames_raw.csv')

ames_1.head()

new_col_names = ames_1.columns.str.lower().str.replace(" ","_")

ames_1.head()
ames_1.columns

ames_1['SalePrice']/1000

# Summary functions

ames_1['SalePrice'].mean()
ames_1['SalePrice'].min()
ames_1['SalePrice'].max()

# Knowledge Check

ames_1['Neighborhood'].mode()

ames_1['Neighborhood'].nunique()

ames_1['Neighborhood'].value_counts()

# Agg method

ames_1[['saleprice' , 'gr_liv_area']].median()

ames_1.agg({'saleprice' : 'mean'})
ames_1.agg({'saleprice' : 'mean', 'gr_liv_area' : 'mean'})


ames_1.agg({'saleprice' : 'mean', 'gr_liv_area' : 'median'})


ames_1.agg({'saleprice' :[ 'max','median','mean'], 'gr_liv_area' : ['mean','median']})


# Knowdledge Check

# Fill in the blan ks to compute average


type(ames_1[['totrms_abvgrd', 'bedroom_abvgr']].mean())

ames_1.agg({'year_built':['mean' , 'median'],'garage_cars' : ['mean','median']})


# Group level aggregation

ames_1.groupby('neighborhood')

ames_1.groupby('neighborhood').agg({'saleprice': 'mean'})

# sort values by sale price

ames_1.groupby('neighborhood').agg({'saleprice': 'mean'}).sort_values(by='saleprice')



ames_1.groupby('neighborhood').agg({'saleprice': ['min','max'],'gr_liv_area':'mean'})



# make neighborhood make one of the column again


ames_1.groupby('neighborhood',as_index=False).agg({'saleprice': 'mean'}).sort_values(by='saleprice')


# Knowledge check - 003

ames_1.groupby(['neighborhood', 'bedroom_abvgr'], as_index=False)

# Compute summary stats
results = ames_1.groupby(['neighborhood', 'bedroom_abvgr'], as_index=False).agg({'gr_liv_area' : 'mean'})

results.head()


cond_a = results['bedroom_abvgr'] ==1

cond_b = results['gr_liv_area'] > 1500

results[cond_a & cond_b]

ames_1.describe()