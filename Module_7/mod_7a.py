import pandas as pd

adult_census = pd.read_csv("C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_7/adult-census.csv")

adult_census

target_column = 'class'
adult_census[target_column].value_counts()



features = adult_census.drop(columns='class')
features.head()
numeric_columns = features.select_dtypes(include=np.number).columns.values
categorical_columns = features.drop(columns=numeric_columns).columns.values

print(f'''
There are {features.shape[0]} observations and {features.shape[1]} features.

Numeric features: {', '.join(numeric_columns)}.

Categorical features: {', '.join(categorical_columns)}.
''')

adult_census.hist(figsize=(20, 14));
adult_census['sex'].value_counts()