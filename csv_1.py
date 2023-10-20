from csv import reader, DictReader


# with open('file.csv','r') as f:
#     read= reader(f)
#     next(read)
#     for i in read:
#         print(i)
with open('file.csv','r') as f:
    read= DictReader(f)
    # next(read)
    for i in read:
        print(i['age'])
