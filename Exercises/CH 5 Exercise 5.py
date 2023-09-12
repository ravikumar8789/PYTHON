def comm(lis, lis1):
    result=[]
    for i in lis:
        if i in lis1:
            result.append(i)
    return result






number1= [1,2,5,8]
number2= [ 2,5,7,9]
print(comm(number1, number2))