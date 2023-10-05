class Laptop:
    def __init__(self, Brand_name,price):
        self.b_name= Brand_name
        self.price=price

    def applied_discount(self,disc):
        
        return f'your amount is  {self.price-((self.price/100)*disc)} rupees after discount'

        

l1= Laptop('HP', 40000)
print(l1.applied_discount(20))