def fibo(ren):
    a=0
    b=1

    if ren==1:
        print("0")
    elif ren==2:
        print("0,1")
    else:
        print("0", end=",")
        print("1", end=",")
        for i in range (0,ren-2):
            c=a+b
            print(c, end=",")
            a=b
            b=c
fibo(10)