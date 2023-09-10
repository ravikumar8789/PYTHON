number= input("Enter a number more then one digit : ")
i=0
sum=0
while i<len(number):
    sum= int(number[i])+sum
    i +=1
print(sum)
