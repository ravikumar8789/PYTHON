while True:
    try:
        age= int(input("Enter your age : "))
        break
    except ValueError:
        print('you have entered non integer value')
    except:
        print('unexpected error')


if age<18:
    print('You are not eledigible')
else:
    print('You are eledigible')