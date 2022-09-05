# We use dictionary where information come as key value pairs
# For example information related to customer like email, Name, address, phone etc.
# Name:Pankaj, so Name is the key, while Pankaj is the value.
# We can define dictionary using curly brackets in the following manner

customer = {"Name":"Pankaj","Email":"vigisbig@gmail.com","Occupation":"Investor","is_verified":True,"age":36} 

# all these keys need to be unique, so, there can not be two Name or Occupation etc. in a dictionary.
# values can be anything, like boolean, string, a list etc.
# We can access these values in the following manner using square brackets

print(customer["Name"])
print(customer["Email"])
#print(customer["Birthyear"])     # This will give us keyerror since this key does not exist

print(customer.get("Birthyear"))     #   We can therefore use get method to call a key and it will give value None and not error
print(customer.get("Birthyear","1986")) # instead of None value, we can also pass a default value if we like

customer["Name"] = "Kiran"          #    We can also update the dictionary value in this way

print(customer["Name"])

customer["Birthyear"] = 1879    #    We can also add new key and its value to a dictionary in this way

print(customer["Birthyear"])