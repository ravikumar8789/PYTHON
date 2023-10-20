f= open('file.txt','r')
# print(f.read())
# print(f.tell())
# f.seek(0)
# print(f.tell())

# print(f.readline())
lis=f.readlines()
# print(lis)
# for line in lis:
#     print(line, end='')
# print(f.name)

for line in lis[:2]:
    print(line,end='')
f.close()
# print(f.closed)
