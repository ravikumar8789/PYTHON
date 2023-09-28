# username=['ravi','pintu','loki','shashi','raja']
# key=['kumar','sharma','kamat','kumar','kamat']

# print(dict(zip(username,key)))
# print(list(zip(username,key)))


l1=[1,3,5,7,9]
l2=[2,4,6,8,10]

l=[(1,2),(3,4),(5,6),(7,8),(9,10)]

# print(list(zip(*l)))
# L1=[]
# L2=[]


# for i,j in l:
#     L1.append(i)
#     L2.append(j)

# print(L1)    
# print(L2)

L1,L2= list(zip(*l))
print(L1,L2)
