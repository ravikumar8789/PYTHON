while True:
    try:
        age= int(input("Enter your age : "))
    except ValueError:
        print('you have entered non integer value')
    except:
        print('unexpected error')
    else:
        print(f'you have entered {age}')
        break
    finally:
        print('this is finally block....')


if age<18:
    print('You are not eledigible')
else:
    print('You are eledigible')