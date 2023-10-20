# with open('file.txt') as ravi:
#     data=ravi.read()
#     # print(data)
# print(f'file is closed or not => {ravi.closed}')

f1=open('file.txt','r')
f2= open('file1.txt','r+')
f2.write(f1.read())
# time.sleep(2)
f2.seek(0)
print(f2.read())