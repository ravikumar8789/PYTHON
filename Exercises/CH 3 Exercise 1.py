import random
num= random.randrange(0,100)
# print(num)
guess_number= int(input("Guess a number between 0 to 100"))
if(num==guess_number):
    print("You win")
elif(num<guess_number):
    print("You guessed less number")
else:
    print("you guessed higher nuber")

