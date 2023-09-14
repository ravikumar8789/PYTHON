# def reverse(i):
#     numbers= i[::-1]
#     return numbers

# num=[]
# def reverse(l):
#     i=len(l)-1
#     while(i>=0):
#         num.append(l[i])
#         i=i-1
#     return num

def reverse(l):
    num=[]
    for i in range(len(l)):
        poped= l.pop()
        num.append(poped)
    return num
        

    
    






number= [1,2,3,4,5,6,7,8]

print(reverse(number))