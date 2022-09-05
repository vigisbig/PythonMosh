#numbers = input("Type your number: ")  
#empty = ""
#num_lib = {
#    "1":"One","2":"Two","3":"Three","4":"Four" 
#}
#for i in numbers:
#    empty += num_lib[i] + " "
#print(empty)

#   An Alternate way
numbers = input("Type your number: ")  
empty = ""
num_lib = {
    "1":"One","2":"Two","3":"Three","4":"Four" 
}
for i in numbers:
    empty += num_lib.get(i,"!") + " "
print (f'Your number is {empty}')
