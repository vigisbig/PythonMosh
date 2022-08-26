numbers = ["1", "2", "3", "4"]

print(numbers)

numbers.append("6")                   #    List method used to add value to the end of the list

print(numbers)

numbers.insert(4,"5")                 #    List method to insert value in the middle of the list.
                                      #    4 is the index and 5 is value
print(numbers)                        #    Ctrl + P is the shortcut to access parameter info, and see what
                                      #    does a particular method expects in terms of values. Before using this,
numbers.remove("3")                   #    you need to ensure that cursor is on the method/function

print(numbers)

numbers.clear()                       #     This will remove all values from the list

print(numbers)

numbers = ["1", "2", "3", "4"]

print("1" in numbers)                #     Searches the list for value and returns boolean expression
print("8" in numbers)

print(len(numbers))                  #     Lets you know about how many elements in total in list