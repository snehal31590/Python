import glob
import os

if True:
    print('Coditioal was True')


a = [1,2,3,4]
b = a
print( a is b)

cond = 'New'


if cond:
    print(' Evaluated to T')
else:
    print('Evaluated to F')
    
## Knowledge Check
x=[3]

if x:
    print('This object contains something')


for number in range(10):
    square = number * number;
    print(f'{number} square = {square}')



squared_values = {}

for number in range(10):
    squared = number * number
    squared_values[number] = squared

squared_values



monthly_data_files = glob.glob("C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_6/monthly_data/*")
monthly_data_files


file_name = os.path.basename(monthly_data_files[0])
file_name



# Range

years = range(2018,2023)
list(years)