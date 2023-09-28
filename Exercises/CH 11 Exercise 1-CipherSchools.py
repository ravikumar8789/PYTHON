def cube(num, *args):
    res=[]
    if args:
        for i in args:
            temp=(i**num)
            res.append(temp)
        return res
    else:
        print("List is empty ")

    









nums=[]
# for i in nums:
#     print(i**3)
print(cube(3,*nums))
