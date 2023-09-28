# def add(*args):
#     t=0
#     for i in args:
#         t = t+i
#     return t


# print(add(1,2,3,4,5))



# kwargs

def prin(**kwargs):
    print(kwargs)
    print(type(kwargs))


names= ['ravi', 'pintu','loki', 'raja']
prin(a=5, b=6, c=7, name="ravi", players=names)