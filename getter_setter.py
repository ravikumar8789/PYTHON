class Treachers:
    def __init__(self, name, age, subject):
        self.name=name
        self._age=max(age, 0)
        self.subject=subject
        # print(f'name of the teacher is {self.name}, age of the teacher is {self._age} and he teaches {self.subject} subject')

    @property
    def complete_detail(self):
        print(f'Name of the teacher is {self.name}, age of the teacher is {self._age} and he teaches {self.subject} subject')
        # print(cls.__name__)    

    
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, new_age):
        self._age=max(new_age,0)



t1= Treachers('Ranjeet sir', 30, 'physics')
t1.age=31
t1.complete_detail