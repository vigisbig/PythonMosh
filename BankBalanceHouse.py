credit_rating = input("Is credit rating good? ")

conv = credit_rating.upper()

if conv == ("GOOD"):
    msg = f"You need to pay 10 % downpayment"
    print(msg)
elif conv == ("BAD"):
    msg = ("You need to pay 20% downpayment")
    print(msg)
