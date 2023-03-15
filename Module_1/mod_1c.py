import random

l_y_w = 185

t_y_w = 190

check = l_y_w > t_y_w

print(check)

# 1 . width and height

width = 3840
height = 2160

pixels = width * height

print(pixels)



# ********************************************88


your_monitor = 3840 *2160
your_monitor


my_monitor = your_monitor
my_monitor


# Check if they have similar values

print(my_monitor == your_monitor)


# Check if it has same object using 'is'
my_monitor is your_monitor


#
your_monitor = 4096 * 2160
your_monitor


print(my_monitor == your_monitor)


my_monitor is your_monitor



# Logical Operators


a = 3
b = 10

c = not((a<5) and (b<5))
print(c)



standard_monitor = 8000000

my_monitor > standard_monitor and your_monitor > standard_monitor


# For atleast one condition
standard_monitor = 8500000
my_monitor > standard_monitor or your_monitor > standard_monitor



# Conditional Statements


level_of_tiredness = "high"

if level_of_tiredness == "high":
    print("Go to bed")
elif level_of_tiredness =="medium":
    print("Read a book")
elif level_of_tiredness =="low":
    print("Go Exercise")
else:
    print("Not a valid input")



 # Knowledge check
import random
random.seed(1)
x = -(random.randint(-10,100))
x


if x > 50:
    print(' x is greater than 50')
elif x < 50 and x >0:
    print('x less than 50 but still positive')
else:
    print('x is negative')


print(4 != 4 or 4 > 5)


x = 5

if x > 50:
    print('x is greater than 50')
elif x > 0:
    print('x is less than 50 but still positive')
elif x == 0:
    print('x is equal to zero')
else:
    print('x is negative')


    
