name = input("What is your name? ")

if len(name) < 3:
    print(f"Name must be atleast 3 characters long!")
elif len(name) > 50:
    print(f"Name cannot be more than 50 characters")
else:
    print(f"Name is oK")