coordinates = (2,3,4)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

# We can assign the values in tuple to x,y,z in above format to avoid repeating again and again
# An alternative to doing it in above format is below, which is short hand and easy. Since we are unpacking the tuple into the three variables
# Hence the name of the file - Unpacking

x,y,z = coordinates

print(x)

# The above method can also be used with lists

List = [3,6,7]

a,b,c = List

print(c)