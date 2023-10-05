class Laptop:
    def __init__(self, brand_name, price):
        self.bname=brand_name
        self.p=price
        # print(f'you have selected {brand_name} and the price of the laptop is {price}')


l1= Laptop('Dell vostro', 45000)
l2= Laptop('Predator', 95000)
print(l1.bname)
