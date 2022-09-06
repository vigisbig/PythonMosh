#   A return statement can be used wherever we want the function to return a value if function is called.
#   For example, we may be doing a calculation etc.

def square(number):
    print (number*number)   #   This is a simple example of function, but in real life, this  may be a large piece of code

                            #   We need to use return instead of print, to avoid None in the terminal
                            #   A thing to keep in mind is that all functions return None value by default
                            #   So if we don't use return, the value none is returned by default
                            #   So, after the square function value is printed, none value is passed as argument
                            #   So whenever, calculating something, use a return statement to return the result
print(square(7))



#   So we use following instead
def multiply(number):
    return (number*number)  


print(multiply(7))
