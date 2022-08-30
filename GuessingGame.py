guess_count = 0
guess_limit = 3
secret_number = 9

while guess_count < guess_limit:
    
    guess = int(input("Guess: "))
    guess_count += 1
    
    if guess == secret_number:
        print(f"You guess it right, the secret number is {secret_number}")
        break                                                               # We can use break to terminate the if loop
else:                                                                       # A while loop can also have a else loop
    print("You Lose!")

