class A:
    def a(self):
        print('hello this is a ')

    def hello(self):
        print('hello this is a')
class B:
    def b(self):
        print('hello this is b ')

    def hello(self):
        print('hello this is b')

class C(A,B):
    pass

c_instance= C()
c_instance.b()



