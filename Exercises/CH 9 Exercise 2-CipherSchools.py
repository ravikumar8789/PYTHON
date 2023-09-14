def checker(l):
    return([str(i) for i in l if type(i)==int or type(i)==float])






lis=[True, False, [1,2,3,4], 1.0,'a',"ravi", 98,"pintu",65, 1.009]

print(checker(lis))