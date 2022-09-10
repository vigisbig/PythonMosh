class ShopCart:

    def __init__(self,person,budget):
        self.person = person
        self.budget = budget
    
    def alldetails(self):
        print(f"Hi, I am {self.person} and I've a budget of {self.budget}")
    
    
shopcart1 = ShopCart("Pankaj",105)

shopcart1.alldetails()

shopcart2 = ShopCart("Ajit",190)

shopcart2.alldetails()






