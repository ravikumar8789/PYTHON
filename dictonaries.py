# user= {'name':'ravi', 'age': 23, 'address': 'madhubani'}
# # print(user)

# user2 = dict(name = 'ravi', age = 23)
# print(user['name'])




# info= {
#     'name':'Ravi kumar',
#     'age': 24,
#     'fav footballers':['ronaldo', 'messi', 'ramos', 'benzema'],
#     'fav movie': ['avengers'],

# }


# print(info['fav footballers'])
# users={
#     'u1':{
#         'name':'Ravi kumar',
#         'age': 24,
#         'fav footballers':['ronaldo', 'messi', 'ramos', 'benzema'],
#         'fav movie': ['avengers'],

#     },
#     'u2':{
#         'name':'Ravi kumar',
#         'age': 24,
#         'fav footballers':['ronaldo', 'messi', 'ramos', 'benzema'],
#         'fav movie': ['avengers'],

#     },
#         'u3':{
#         'name':'Ravi kumar',
#         'age': 24,
#         'fav footballers':['ronaldo', 'messi', 'ramos', 'benzema'],
#         'fav movie': ['avengers'],

#     },
# }
# print(users)



# if ['ronaldo', 'messi', 'ramos', 'benzema']in info.values():
#     print("yes")
# else:
#     print("no")

# info_new= info.items()
# print(info_new)
# i=1
# for key,values in info.items():
#     print(f"{i}=> {key} {values}'")
#     i+=1

# for i,K in info.items():
#     print(i,K)

info= {
    'name':'Ravi kumar',
    'age': 24,
    'fav movie': ['avengers'],
    'fav footballers':['ronaldo', 'messi', 'ramos', 'benzema'],

}
dicton= dict(name='ravi', age=24)
# print(dicton)

for i,j in dicton.items():
    print(i,j)
# add information
# info['fav character']= ['ironman', 'batman']
# info['fav footballers']= ['kroos', 'david']

# delete
# print(info.pop('fav movie'))

# poped_item
# p=info.popitem('')
# # print(type(p))
# print(p)
# print(info)


# clear()
# copy()
# get(key)