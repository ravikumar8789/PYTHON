l=['ravi','pintu','loki','shashi','raja']
# for i, j in enumerate(l):
#     print(f"{i}=={j}")



# def location(l, name):
#     for i,j in enumerate(l):
#         if j==name:
#             return i
#     return -1    
# print(location(l,'shashi'))


def location(l, name):
    return (i for i,j in enumerate(l) if j==name ) 
print(location(l,'shashi'))