#numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# numbers=[]
# for i in range(1,21):
#     numbers.append(i)

numbers=[i for i in range(1,21)]

# def is_even(num):
#     return num%2==0
# list(filter(lambda num: num%2==0, numbers)):
for i in list(filter(lambda num: num%2==0, numbers)):
    print(i)