import pandas as pd

ames_1 = pd.read_csv('C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_3/ames_raw.csv')

ames_1.head()

new_col_names = ames_1.columns.str.lower().str.replace(" ","_")

ames_1.columns
ames_1.columns = new_col_names

# Can use rename which uses dictionary, if you don't use columns while renaming then it will change the indexes

ames_1.rename(columns = {'ms_zoning': 'municipality_zoning'})

# Adding and Removing Columns

new_price = ames_1['saleprice'] / 1000

# Each realtor collectod 3 percent

new_cal_price = sum(ames_1['saleprice'] *0.03)

# Add a column names

ames_1['sales_commission'] = ames_1['saleprice'] *0.03
ames_1.head()

# drop columns
ames_1.drop(columns=['sales_commission' , 'saleprice'])

#Calculate sum

new_price_sum =  ames_1['']



# Knowledge check

# A. Create a new column utility_space that is 1/5 of the above ground living space
ames_1['utility_space'] = ames_1['gr_liv_area'] * 1/5
ames_1.head()


# 2. Round above o/p

ames_1['utility_space'] = round(ames_1['gr_liv_area'] * 1/5)
ames_1.head()

new_ames_11_1 = ames_1.drop(columns= 'utility_space')

new_ames_11_1.head()



# Calculating with Multiple columns

ames_1['price_per_sq_ft'] = ames_1['saleprice'] / ames_1['gr_liv_area']
ames_1.head()


# Vector scalar mathematical operation

ames_1['price_per_sq_ft'] = (ames_1['sales_price_k']*1000) / ames_1['gr_liv_area']
ames_1.head()


# Knowledge Check
# Create a new column price_per_total_sqft



total_sqft = ames_1['saleprice'] / (ames_1['gr_liv_area'] +ames_1['total_bsmt_sf'] + ames_1['wood_deck_sf'] + ames_1['open_porch_sf'])

ames_1['price_per_total_sqft'] =  ames_1['saleprice'] / total_sqft