#***************ROUND FUNCTION******************
x = 2.9                 #   variable x and value assigned
print(x)

y = round(x)            #   Round function is an inbuilt function and it rounds the value of x
print(y)

print(round(x))         #   You can either use it this way or as way specified above

#****************ABS FUNCTION*******************
x = -19

print(abs(x))           #   Round function always returns a positive value.

# If you want to write a program that needs complex mathematical calculations, we will need to import math module.
# It has reusable functions that we can use for mathematical calculations

import math             #   Imports math module.
print(math.ceil(3.7))   #   Math is now an object, so we can use its methods using the dot operator.
print(math.floor(3.8))
