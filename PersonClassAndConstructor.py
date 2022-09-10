class Person:
    def __init__(self,n,a):
        self.name = n
        self.age = a

    def talk(self):
        print(f"Hi I am {self.name}")       


person1 = Person("Pankaj",36)
print(person1.name)
print(person1.age)
person1.talk()