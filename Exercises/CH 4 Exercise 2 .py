def is_palindrome(name):
    if name[::-1]==name:
        return "yes i am palindrome"
    return "no i am not palindrome"

nm= input("Enter a name : ")
print(is_palindrome(nm))
