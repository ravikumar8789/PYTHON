def list_counter(lis):
    count=0
    for i in lis:
        if type(i)==list:
            count= count+1
    return count






number= [1,2,3,4,[1,2,3], [2,5,7],[7,9,0]]

print(list_counter(number))