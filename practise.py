guess_count = 3
count = 0
secret_number = 8

while count < guess_count:

    num = int(input("Enter number: "))
    count +=1

    if num == secret_number:
        print("That's a correct guess")
        break
else:
    print("You lose")