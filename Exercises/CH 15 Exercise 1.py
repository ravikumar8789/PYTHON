def gen(num):
    for i in range(1,num+1):
        if i%2==0:
            yield i
    # (yield i for i in range(1,num+1) if i%2==0)

# gen(10)

for i in gen(10):
    print(i)