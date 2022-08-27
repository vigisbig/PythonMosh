price = 10                                                  #   This is an example of Integer
rating = 4.9                                                #   This is an example of Float
name = input("What is your name? ")                         #   This is an example of String, Input function
is_published = True                                         #   This is an example of Boolean
                                                            #   For defining variables, we should use lower case letters,
                                                            #   special keywords however,
                                                            #   Should have the first letter as block like True, False etc.
color = input("Hi " +name +"! What is your favourite color? ") #   Print function used for gathering input

print(name + " likes "+  color)
print(type(name), type(color))                              # Type function tyring to find variable type of name and color

print("We'll use double quote in some places")             # We do this to avoid confusing python"
print('And in some places, we will use "single" quotes')   # We do this to avoid confusing python"
print("""We'll need to use triple double quotes if we're to show both "double" and 'single' quotes in message""")
print('''Or We'll need to use triple single quotes if we're to show both "double" and 'single' quotes in message''')

# We can use triple double quotes or triple single quotes too for strings that have single and double quotes