class Tails:                   
    def tail(self):
        print("tail")

class Mammals:
    def walk(self):
        print("walk")

class Dog(Mammals,Tails):
    pass
class Cat(Mammals,Tails):
    pass

dog1 = Dog()
dog1.tail()
dog1.walk()