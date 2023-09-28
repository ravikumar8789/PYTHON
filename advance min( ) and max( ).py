# names=['ravikumarthakur','kumar','thakur','hellodaddy']


# def mx(name):
#     return len(name)


# # print(min(names))
# print(mx(names))
# print(max(names, key=lambda nm: len(nm)))

# def fun(data):
#     return data.get('score')


data1= [
    {'name': 'ravi', 'age':23, 'score':100},
    {'name': 'pintu', 'age':20, 'score':85},
    {'name': 'loki', 'age':19, 'score':75}
    
]

# print(max(data1, key=lambda i: i.get('score') ))

# print(sorted(data1, key= lambda d : d['age'],reverse= True))



# lis=[2,5,9,3,8,4,7,1]
# print(sorted(lis, reverse=True))


sen= "ravi KumAr"
se=''
print(sen.swapcase())
for i in sen[]:
    se.join(i)
