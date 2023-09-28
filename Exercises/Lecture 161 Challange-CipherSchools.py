l1=[2,3,4]
l2=[4,6,8]


# def af(l1,l2):
#     avg=[]
#     for i in zip(l1,l2):
#         avg.append(sum(i)/len(i))
#     return avg

# af=lambda l1,l2 :[sum(i)/len(i) for i in zip(l1,l2)]
# print(af(l1,l2))

# avg= lambda *args: [sum(i)/len(i) for i in zip(*args)]
# print(avg(l1,l2))


# l= [1,2,3,4,5,6,7,9]
# names=['ravi', 'kumar', 'thakur']

# print(any([i[-1]=='i' for i in names]))

# print(any([l]))
# print(any([i%2==0 for i in l]))
# print(all([True ,False ,True ,True ,True]))

# def add(*args):
#     total=0
#     if all([type(i)==int or type(i)==float for i in args]):
#         for i in args:
#             total+=i
#     else:
#         return 'invalid input'
#     return total


# def add(*args):
#     total=0
#     if all([type(i)==int or type(i)==float for i in args]):
#         for i in args:
#             total +=i
#     else:
#         return 'invalid input'
#     return total

# print(add(1,2,3,4,5,23.1,'ravi'))
