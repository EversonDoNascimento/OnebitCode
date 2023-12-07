def uppercase_decorator(func):
    def wrapper():
        return func().upper()
    return wrapper

def split_decorator(func):
    def wrapper():
        return func().split()
    return wrapper

@split_decorator
@uppercase_decorator
def func_decorator():
    return "Hello World"

print(func_decorator())