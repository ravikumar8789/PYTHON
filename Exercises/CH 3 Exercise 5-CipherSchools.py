name=input("Enter your name : ")
# c= 'a'
i=0
temp=""
while i<len(name):
    if name[i] not in temp:
        temp= temp+name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i +=1

