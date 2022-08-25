course = ("Python for you")

# the course variable here is technically storing a String object.
# And an object can have many capabilities, like remote changing volume, changing channel, turning OFF etc.
# You can access these string specific functions (appropriately known as methods)
# by adding a dot followed by the string variable as below. These are called methods and not functions
# since functions are more generic and methods are specific. So functions, when part of an object are called methods
print(course.upper())
print(course)
# note that the string variable itself does not change with use of these methods.
print(course.lower())
print(course.find('y')) # is used to find the occurence of y, so the index 0,1,2,3 returns the value 1
print(course.find('Y')) # Due to case sensitive nature we get -1, since there's no capital Y
print(course.find('for')) # returns index for word for and reports its first occurence
print(course.replace('for', '4')) # this will also not modify the original string.
print(course.find('Python')) # finds the word python, and returns its index of its first occurence
print('Python' in course) # returns boolean value instead of index
