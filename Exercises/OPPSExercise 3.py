class Person:
    count=0
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        Person.count+=1
    

p1=Person('ravi',63)
p1=Person('ravi',63)
p1=Person('ravi',63)
p1=Person('ravi',63)
p1=Person('ravi',63)

print(Person.count)
