def market(pulses,soap,namkeen,shipping):
    print(f"You have bought things worth {pulses}, {soap}, {namkeen}, {shipping}")

#   Below is the format of using keyword arguments, this can clarify the code
#   We use mostly positional argument, but in case to make it easy readable, we may also use keyword arguments sometimes
#   Since these are keyword arguments, their relative position does not matter, they improve readability also unlike positional arguments



market(namkeen="40$",pulses="50$",shipping="4$",soap="12$")     

#   We can use positional arguments with keyword arguments, but keyword arguments must always be used after positional arguments like below
#   Use of keyword argumnets before positional arguments will give error.

market("50$","12$","40$",shipping="4$")

market(shipping="4$","50$","12$","40$")     #   This will not work however and will give error

