#   We can also pass information to functions when we define parameters while defining them
#   These parameters serve as placeholders for receiving information
#   Below you can see name used a parameter for welcome_greeting function

def welcome_greeting(name):
    print(f"Hello how are you Mr {name}")

#   Argument is the value supplied to the function. Below you can see we have used the argument Pankaj passed to the function
#   Important to note that argument is value passed to function, parameter is placeholder in a function for receiving information,
#   While argument is actual information supplied to the function. So, name is parameter while Pankaj is argument

welcome_greeting("Pankaj")