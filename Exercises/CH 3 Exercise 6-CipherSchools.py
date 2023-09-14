import random
rand1= random.randint(1, 100)
count= 0
num= -1
while num!=rand1:
    num= int(input("Guess a number : "))
    if num<rand1:
        print("too low")
        count +=1
    elif num>rand1:
        print("too high")
        count +=1
    else:
        count +=1
        print(f"you won in {count} times")

