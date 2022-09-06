def welcome_full(first_name,last_name):
    print(f"Hello {first_name} {last_name}, How are you?")
    print("Welcome to the Ship!")

#   Whatever, parameters we have defined in a function, we must pass the relevant arguments aka positional arguments for them, else we are going to get error.
#   Second call of functions shows that example and gives that error ans says that positional argument required

welcome_full("Pankaj","Vig")
welcome_full("Ajit")