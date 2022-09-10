class Tails:                   
    def tail(self):
        print("tail")

class Mammals:
    def walk(self):
        print("walk")

class Dog(Mammals,Tails):
    pass                                # A class cannot be empty, so we input pass which tell python to skip this, it's ok.
class Cat(Mammals,Tails):
    pass

dog1 = Dog()
dog1.tail()
dog1.walk()