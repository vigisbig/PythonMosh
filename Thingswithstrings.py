course = "Python for you"

# the course variable here is technically storing a String object.
# And an object can have many capabilities, like remote changing volume, changing channel, turning OFF etc.
# You can access these string specific functions (appropriately known as methods)
# by adding a dot followed by the string variable as below. These are called methods and not functions
# since functions are more generic and methods are specific. So functions, when part of an object are called methods
print(course)
# note that the string variable itself does not change with use of these methods.
print(course.upper())
print(course.lower())
print(course.find('y')) # is used to find the occurrence of y, so the index 0,1,2,3 returns the value 1
print(course.find('Y')) # Due to case-sensitive nature we get -1, since there's no capital Y
print(course.find('for')) # returns index for word for and reports its first occurrence
print(course.replace('for', '4')) # this will also not modify the original string.
print(course.find('Python')) # finds the word python, and returns its index of its first occurrence
print('Python' in course)   # in is a special keyword in Python called in operator, and it returns boolean
                            # value instead of index
print(course[0])       # finds the letter with index 0
print(course[-1])      # finds the letter with index -1
print(course[0:6])     # finds all letters with index 0 till index 5
print(course[0:])      # finds all letters starting from index 0 till end
print(course[3:])      # finds all letters starting from index 3 till end
print(course[:6])      # finds all letters starting from index 0 till index 5
print(course[:])       # finds all letters starting from index 0 till end
print(course[1:-1])    # finds letters starting from index 1 till -1 (-1 index letter not included)
print(len(course))     # We can use len function to find out lengths of strings. It's a general purpose function
print(course.replace('you','beginners'))