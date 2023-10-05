def gen(n):
    for i in range(1,n+1):
        yield i
    


numbers=gen(10)

for i in numbers:
    print(i)
for i in numbers:
    print(i)

