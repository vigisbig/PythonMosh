#   A sucessful program runs and returns the exit code 0
#   If it crashes, it will return exit code 1 or other code, so we have to prevent this
#   Try - except is a construct in Python that helps avoid errors and prevent program from crashing
#   You can see the sample program below that handles ValueError
try:
    Age = int(input("Age: "))
    print(Age) 
except ValueError:
    print("Not a valid value")
