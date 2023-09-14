# for i in range(10):
#     print(f"hello python {i}")

# for i in range (1,10+1):
#     print(f"hello python {i}")


# name = input("Enter your name : ")
# temp = ""
# for i in range(len(name)):
#     if(name[i] not in temp):
#         print(f"{name[i]}:{name.count(name[i])}")
#         temp= name[i]+temp

# name = input("Enter your name: ")
# temp = ""
# for i in range(len(name)):
#     if name[i] not in temp:
#         temp += name[i]
#         count = name.count(name[i])
#         print(f"{name[i]}:{count}")


number= input("Enter a number : ")
sum=0
for i in number:
    sum= int(i)+sum
print(sum)