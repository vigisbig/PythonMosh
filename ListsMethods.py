numbers = ["1","2","3","4","3"]

print(numbers)

numbers.append("6")                  #    List method used to add value to the end of the list

print(numbers)

numbers.insert(4,"10")               #    List method to insert value in the middle of the list.
                                     #    4 is the index and 5 is value
print(numbers)                       #    Ctrl + P is the shortcut to access parameter info, and see what
                                     #    does a particular method expects in terms of values. Before using this,
numbers.remove("3")                  #    you need to ensure that cursor is on the method/function

print(numbers)

numbers.clear()                      #     This will remove all values from the list

print(numbers)

numbers = ["1", "2", "3", "4"]

numbers.pop()                        # By default pop method removes the last value, but you can also pass idex value to remove particular item (like below)

print(numbers)

numbers.pop(2)

print(numbers)

numbers = ["1", "4", "3", "2","4","4"]

print("1" in numbers)                #     Searches the list for value and returns boolean expression
print("8" in numbers)

print(len(numbers))                  #     Lets you know about how many elements in total in list

print(numbers)

print(numbers.index("3"))            #     This will print the index where the item 4 first presents
#print(numbers.index("19"))          #     Since the number is not present, we get an error, so we can use "in" instead.
                                     #     This will give boolean output as above, and will return true or false

print(numbers.count("4"))            #     Counts the number of times the particular value occurs 

print(numbers.sort())                #     Sort for sorting elements in a list. 
                                     #     Sort is the method which does not accept any value, so when we print it, it return none. 
                                     #     We can therefore use it without print as below
numbers.sort()

print(numbers)                      

numbers.reverse()                                     #     We can use reverse, followed by sort to reverse the order

print(numbers)
