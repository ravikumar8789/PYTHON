# numbers= [1,2,3,4,5,6,7]
# print(numbers)

# name= ["ravi", "raja", "pintu", "loki", "ravi"]
# age=[23, 23, 20, 19]
# print(name)

# mixed=[ "ravi", 7 , "loki", 8]
# print(mixed)

# print(name[-1:-4:1])

# fuctions
# name[1:3]= "ravi"
# name[1:3]= ["krishna", "pradushan"]
# name.append("ritesh") last position
# name.insert(0, "shashi")  insert at any point
# nm= name+age #adding two string
# print(nm)

# name.extend(age)
# name.append(age)
# name.reverse()
# print(name.count("ravi"))
# name.pop()
# name.sort()
# print(sorted(name))
# name.clear()
# cpy= name.copy()

# print(cpy)

# line= "hello sendrela how are you".split()
# print(line)

# str1='stte'
# str1[2]='k'
# print(str1)

# matrix= [[1,2,9], [4,5,6], [7,8,9]]
# for i in matrix:
#     for j in i:
#         print(j)

# print(matrix)
# print(matrix[0])

# print(len(matrix))
# for i in matrix:
#     print(i)
# j=3
# for j in matrix:
#     print(j)
#     break
# print(name)
# numbers=[]
# length=int(input("Enter the size of list : "))
# for i in range(0,length):
#     ele= int(input())
#     numbers.append(ele)

# print(numbers)



# lst = []
# n = int(input("Enter number of elements : "))
 
# for i in range(0, n):
#     ele = [input(), int(input())]
#     lst.append(ele)
 
# print(lst)
# creating an empty list
# lst = []
 
# # number of elements as input
# n = int(input("Enter number of elements : "))
 
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#     # adding the element
#     lst.append(ele) 
 
# print(lst)


# number= list(range(1,20))
# print(number)
# numbers = [1,2,3,4,5,6,7,8,9]

# def neg(l):
#     for i in l:
#         print(numbers.index(i))

# neg(numbers)



# a=[]
# for i in range(int(input("numbers of element : "))):
#     a.append(int(input()))

# print(a)
# ???????????????????????????????????????????????????????????????????????????????????
# ???????????????????????????????????????????????????????????????????????????????????



# list comprehension

# lis=[]
# for i in range(1, 11):
#     lis.append(i*i)

# print(lis)


# sq=[i**2 for i in range(1,11)]
# print([i**2 for i in range(1,11)])


# print([i*-1 for i in range(1,11)])


# name=['ravi', 'pint', 'loki', 'raja']

# print([i[0] for i in name])


# nums=[1,2,3,4,5,6,7,8,9,10]

# print([i for i in range(1,11) if i%2==0])

# print([i*2 for i in nums if i%2==0 else: -1]) =======wrong




# print([i*2 if i%2==0 else -i for i in nums])



# print([[i for i in range(1,4)] for i in range(3)])
print([[i for i in range(1,4)] for i in range(3)])
