# def add(num1, num2):
#     return num1+num2



# a = int(input("Enter a number : "))
# b= int(input("Enter a number : "))

# print(add(a,b))


# def last_char(name):
#     return name[-1]


# nm= input("enter a name : ")
# print(last_char(nm))






# def odd_even(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")


# number= int(input("Enter a number : "))
# odd_even(number)



def greater(num1, num2):
    if num1 >num2:
        return num1
    return num2

def ngreater(n1, n2, n3):
    bigger= greater(n1,n2)
    return greater(bigger,n3)


print(ngreater(40,20,30))


