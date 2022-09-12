import random

class Dice:                                         # Creating a class Dice
    def roll(self):                                 # Defining a method roll
        p = random.randint(1,6)
        q = random.randint(1,6)
        return p,q

dice = Dice()                                       # Creating an object dice of class Dice

print(dice.roll())                                  # Calling method .roll