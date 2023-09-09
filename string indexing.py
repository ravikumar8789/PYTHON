# lang= "Ravikumar"
# print(lang[5])
# print(lang[-10])

# print(lang[2:8])
# print(lang[9::-1])

palin= input("Enter any string to check weather it is palindrome or not : ")
res= palin[: : -1]
if(palin==res):
    print("yes i am palindrome")
else:
    print("no i am not palindrome")
