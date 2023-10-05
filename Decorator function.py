from functools import wraps
# def decorator(func):
#     @wraps(func)
#     def randomfunc(*args, **kwargs):
#         """ this is decorator function"""
#         print('this is awsome function')
#         return func(*args, **kwargs)
#     return randomfunc
# @decorator
# def f1():
#     print('this is function 1')


# @decorator
# def f2():
#     print('this is function 2')




# a=decorator(f1)
# a()
# f2()
# f1()

# f1=decorator(f1)
# f1()



# @decorator
# def info(age):
    # '''this is information function '''
    # print(f'hello my name is ravi kumar and my age is {age}')

# info(21)
# print(info.__doc__)
# print(info.__name__)



# @decorator
# def add(a,b):
#     return a+b


# print(add(2,3))
# def printfunctiondata(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'you are calling {func.__name__} function')
#         print(func.__doc__)
#         return func(*args, **kwargs)
#     return wrapper



# @printfunctiondata
# def add(a,b):
#     '''this function takes two arguments and sum them'''
#     return a+b

# print(add(4,5))
# print(add.__doc__)


# def only_int(func):
#     @wraps(func)
#     def wrap(*args, **kwargs):
        # dt=[]
        # for i in args:
        #     dt.append(type(i)==int)
        # if all(dt):
        #     return func(*args, **kwargs)
        # else:
        #     return ('invalid input')
#         if all([type(i)==int for i in args]):
#             return func(*args, **kwargs)
#         return 'invalid argument'
#     return wrap

# @only_int
# def add(*args):
#     tot=0
#     for i in args:
#         tot+=i
#     return tot

# print(add(1,2,3,4,5,'ravi'))


# def dec(func):
#     @wraps(func)
#     def wrappers(*args, **kwargs):
#         dt=[]
#         for i in args:
#             dt.append(type(i)==int)
#         if all(dt):
#             return func(*args, **kwargs)
#         else:
#             return 'invalid input'
#     return wrappers

# @dec
# def add(*args):
#     total=0
#     for i in args:
#         total+=i
#     return total

# print(add(1,2,3,4,5,'ravi'))




def only_data_type(dt):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            datatype=[]
            for i in args:
                datatype.append(type(i)==dt)
            if all(datatype):
                return function(*args,**kwargs)
            else:
                return 'invalid'
        return wrapper
    return decorator
    


@only_data_type(int)
def add(*args):
    total=0
    for i in args:
        total+=i
    return total




print(add(1,2,3,4,5))