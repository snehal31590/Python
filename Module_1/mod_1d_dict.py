# Dictionaries are mutable
# dynamic i.e can grow and shrink
# Can be nested

d = { 'first_name' : 'Snehal' , 'last_name' : 'Lokhande'}

type(d)
d['alma_mater'] = 'UoP'
d

# Dictionaries have diff methods of storing the values
# 'Hash table look up' procedure
# Within a list we have to iterate over every single element.

d['first_name']

# Dictionaries have several diff methods, get items with .items() which will return a list

d.items()

# Knowledge Check 

# Create a dict ceo

ceos = {'Apple':'Time Cook' , 'Microsoft' : 'Satya Nadella'}


type(ceos)

ceos['Apple']

# Add a new element to dict
ceos['Disney'] = 'Bob Iger'
ceos

# update disnet ceo to releft the change

ceos['Disney'] = 'Bob Chapek'
ceos



letters = ['a', 'b', 'c', 'd', 'e']
letters[3]


instructors = {'brad': {'first_name': 'Brad',
  'last_name': 'Boehmke',
  'alma_mater': 'NDSU',
  'employer': '84.51˚',
  'zip_code': 45385},
 'ethan': {'first_name': 'Ethan',
  'last_name': 'Swan',
  'alma_mater': 'Notre Dame',
  'employer': '84.51˚',
  'zip_code': 45208}}


instructors['ethan']['alma_mater']