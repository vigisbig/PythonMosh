numbers = range(5)              #  A range function is an object that can store a sequence of values

print(numbers)                  #  Displays the range object in its default representation format i.e. range (0, 5)
for number in numbers:          #  To see the complete list of range items, you will need to use for loop
    print(number)               # the range (0,5), creates 5 values i.e. 0-4 using 1 as a step (and excludes 5)

numbers = range(5,10)

print(numbers)                  #  Displays the range i.e. range (5, 10)
for number in numbers:          # Displays the range items
    print(number)

numbers = range(5,10,2)         # Instead of a normal step of 1, it uses a step of 2 for creating a range

print(numbers)
for number in numbers:          # Displays the range items
    print(number)

print("******************")     # Displays *********** for differentiation
for number in range(4,20,2):         # This is a direct way of declaring a range without have to declare a variable numbers
    print(number)




