def division():
    try:
        num1=int(input("Enter a number : "))
        num2= int(input('Enter another number to divide :'))
        result= num1/num2
    except ZeroDivisionError:
        print('Please dont divide by zero')
    except ValueError:
        print('Please enter only integeral value')
    else:
        print(result)
    


division()

         