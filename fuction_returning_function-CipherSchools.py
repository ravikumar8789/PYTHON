# def square(a):
#     return a**2
lis=[1,2,3,4,5,6,7,8,9]
# print(list(map(square,lis))) 


# def msq(func, a):
#     lsi=[]
#     for i in a:
#         lsi.append(func(i))
#     return lsi


# print(list(msq(lambda a:a**2,lis)))


# def of():
#     def innerf():
#         print('hello ravi')
#     return innerf


# of()


# def of(msg):
#     def innerfunc():
#         print(f"hello message is delevered. and the message is : {msg}")
#     return innerfunc

# a= of('i love you')
# a()


def calc(base):
    def p():
        return base**4
    return p



a=calc(4)
print(a())
        
    





















