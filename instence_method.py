class person:
    def __init__(self, first_name, last_name):
        self.fname= first_name
        self.lname= last_name
    def full_name(self):
        return (f'{self.fname} {self.lname}')
    

# print(person.__init__('ravi', 'kumar'))
# print(p1.full_name)

p1= person('ravi','kumar')
print(person.full_name(p1))
# print(p1.full_name())


# l=[1,2,3,4]
# list.append(l,10)
# print(l)