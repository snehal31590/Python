from multiprocessing.spawn import import_main_path


p_rest_bp_male = heart_1.loc[heart_1['sex'] == 'Male']
p_rest_bp_male_selected = p_rest_bp_male[['sex', 'rest_bp']]
p_rest_bp_male_selected.head()
print("The mean resting blood pressure for males is",p_rest_bp_male_selected['rest_bp'].mean())


p_rest_bp_female = heart_1.loc[heart_1['sex'] == 'Female']
p_rest_bp_female_selected = p_rest_bp_female[['sex', 'rest_bp']]
p_rest_bp_female_selected.head()
print("The mean resting blood pressure for females is",p_rest_bp_female_selected['rest_bp'].mean())


p_chol_male = heart_1.loc[heart_1['sex'] == 'Male']
p_chol_male_selected = p_chol_male[['sex', 'chol']]
p_chol_male_selected.head()
print("The mean resting blood pressure for males is",p_chol_male_selected['chol'].mean())


p_chol_female = heart_1.loc[heart_1['sex'] == 'Female']
p_chol_female_selected = p_chol_female[['sex', 'chol']]
p_chol_female_selected.head()
print("The mean resting blood pressure for females is",p_chol_female_selected['chol'].mean())


# Alternate solution -
p_agegroup_male = heart_1.loc[heart_1['sex'] == 'Male']
p_agegroup_male_selected = p_agegroup_male[['sex', 'chol','age']]
p_agegroup_male_selected.head()

p_agegroup_male_selected_med= p_agegroup_male_selected.groupby('age').agg({'chol': ['median']})
p_agegroup_male_selected_med
print("Age group 77 has the largest median cholesterol levels for males",p_agegroup_male_selected_med)
# Above is invalid

m_c_l = heart_1.groupby(['age' , 'sex'],as_index=False).agg({'chol':'median'})
m_c_l.loc[m_c_l['sex'] == 'Male']

sorted_v = m_c_l.sort_values(by='age', ascending=False)
sorted_v
print("Age group that has the largest median cholesterol levels for males",sorted_v.loc[72])

# 4.
mean_age_sex_each = heart_1.groupby(['age' , 'sex'],as_index=False).agg({'risk':'mean'})
mean_age_sex_each
mean_age_sex_each_sorted = mean_age_sex_each.sort_values(['age', 'sex'],ascending=False)
print("The mean risk value for each age and sex is ",mean_age_sex_each_sorted)


heart_1.columns
com_mean_risk = heart_1['risk'].mean()
com_mean_risk

p_risk_male = heart_1.loc[heart_1['sex'] == 'Male']
p_risk_male_selected = p_risk_male[['sex', 'risk','age']]
p_risk_male_selected






n_1 = p_risk_male_selected.groupby('age').agg({'risk' : ['mean']})

heart_1
#result_3_1 = heart_1.groupby('sex').agg({'rest_bp' :'mean'}).sort_values(by='rest_bp')







import_main_path

# 2.
result_3_2 = heart_1.groupby('sex').agg({'chol' :['mean' ,'median']})
print("the mean and median cholesterol levels for males and females",result_3_2)


# 3. 

#result_3_3_1 = heart_1.groupby('age').agg({'chol' :['mean' ,'median']})
#result_3_3_1.sort_values(by='age')

m_c_l = heart_1.groupby(['age' , 'sex'] ,as_index=False).agg({'chol':'median'})
m_c_l_1 = m_c_l.loc[m_c_l['sex'] == 'Male']


sorted_v = m_c_l_1.sort_values(by='age', ascending=False)
sorted_v.max()
print("Age group that has the largest median cholesterol levels for males",sorted_v.max())


# 4.  Compute mean risk value (the risk column was created in problem 2 of the "Manipulating data"section) for each age and sex. Which gender and age group has the highest average risk value?
mean_age_sex_each = heart_1.groupby(['age' , 'sex'],as_index=False).agg({'risk':'mean'})
mean_age_sex_each
mean_age_sex_each_sorted = mean_age_sex_each.sort_values(['age', 'sex'],ascending=False)
mean_age_sex_each_sorted
type(mean_age_sex_each_sorted)
mean_age_sex_each_sorted.max()
print("The mean risk value for each age and sex is ",mean_age_sex_each_sorted)
