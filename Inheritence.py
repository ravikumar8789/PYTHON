import time
class Teachers:
    def __init__(self, name, subject, age):
        self.name= name
        self.subject= subject
        self.age=age
        self.complete_information= f'name is {self.name}, subject he teaches is {self.subject} and age is {age } years'


    def printing_age(self):
        print(f'printing his age....')
        time.sleep(2)
        print(f'Age is {self.age}')


class Teachers_singers(Teachers):
    def __init__(self, name, subject, age,instrument):
        super().__init__(name, subject, age)
        
        self.instrument= instrument

    def print_all_details(self):
        print(f'This teacher is also singer and can play {self.instrument} ')




t1= Teachers('ranjeet sir ','physics', 30)
t2=Teachers_singers('Manisha mam', 'Music', 35, 'Harmonium')


print(t1.complete_information)
t1.printing_age()

print(t2.complete_information)
t2.printing_age()
t2.print_all_details()
