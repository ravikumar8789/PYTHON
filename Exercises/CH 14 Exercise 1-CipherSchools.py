import time
from functools import wraps

# def calculate_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'we are calling the {func.__name__} function')
#         t1= time.time()
#         a= func(*args, **kwargs)
#         t2=time.time()
#         total_time= t2-t1
#         print(f'this function took {total_time} seconds to finish the execution')
#         return a
#     return wrapper



# l=[1,2,3,4,5,6,7,8,9]

# @calculate_time
# def add(k):
#     return [i**2 for i in range(1,k)]


def dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1= time.time()
        z= func(*args, **kwargs)
        t2=time.time()
        print(f'this function takes {t2-t1} second')
        return z
    return wrapper



# add(1000000)
    

# t2= time.time()
@dec
def add(k):
    return [i**2 for i in range(1,k)]



add(1000000)

# print(add(l))
# print(f'this function takes {t2-t1} second to execute')