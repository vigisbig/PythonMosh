                                        #       Tuples are like lists, we use them to store a sequence of objects.
                                        #       Unlike lists Tuples are immutable though, i.e we cannot change them
numbers = (1,2,4,4,5,7,4,8,4)           #       In case of tuple, we use nomral bracket

#numbers[1] = 10                        #       This will not work since Tuple is immutable
                                        #       Methods like append, insert, remove are not available in tuple
print(numbers.count(4))                 #       Displays count of 4 occurrence

print(numbers.index(4))                 #       Gives the index of occurence of 1st element