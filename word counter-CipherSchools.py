def counter(name):
    dic={}
    for i in name:
        temp=name.count(i)
        dic[i]= temp
    return dic

print(counter("ravi kumar"))
    