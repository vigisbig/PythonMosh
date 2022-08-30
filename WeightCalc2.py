weight = float(input("What is your weight? "))
unit = input("(K)g or (L)b? ")

if unit.upper() == "K":

    WP = weight / 0.45

    print(f"Weight in pound is {WP} Pound")                 # Done using formatted strings

else:

    WK = weight * 0.45

    print("Weight in kg is " + str(WK) + " Kilogram")       # Done using string concatenation
    