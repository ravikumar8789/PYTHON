class Person:
    new_age=20
    def __init__(self, name, age, vill):
        self.name=name
        self.age=age
        self.vill= vill
    def age_increment(self):
        return self.age+self.new_age
    


p1=Person('ravi',23,'jafra')
# p1.new_age=10
print(p1.age_increment())
