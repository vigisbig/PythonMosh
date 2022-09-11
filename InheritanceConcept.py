class Tails:                   
    def tail(self):
        print("tail")

class Mammals:
    def walk(self):
        print("walk")
                                        # A class cannot be empty, so we input pass which tells python to skip this, it's ok.
class Dog(Mammals,Tails):               # To the dog class we have inherited Mammals and Tails class, so we will be able to 
    pass                                # use methods of these classes in dog object too.
class Cat(Mammals,Tails):               # To the cat class too, we have inherited Mammals and Tails
    def meow(self):
        print("meow")


dog1 = Dog()                            # Creating an instance of Dog class
dog1.tail()                             # Calling tail method defined in Tails
dog1.walk()                             # Calling walk method defined in Mammals

cat1 = Cat()                            # Creating an instance of Cat class
cat1.meow()                             # Using method in Cat class
                                        