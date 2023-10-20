# with open(r'G:\PYTHON\Exercises\EXFile.txt') as f1:
#     with open(r'G:\PYTHON\Exercises\EXfile1.txt','a') as f2:
#         data=f1.readline().split(',')
#         f2.write(f'{data[0]} salary is {data[1]}')

with open(r'G:\PYTHON\Exercises\EXFile.txt') as f1:
    with open(r'G:\PYTHON\Exercises\EXfile1.txt','a') as f2:
        for i in f1.readlines():
            name,salary= i.split(',')
            f2.write(f'{name}\'s salary is {salary}')