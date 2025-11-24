
def decoration(func):

    def wrapper(*args, **kwargs):
        print("Before function run")
        result = func(*args, **kwargs)
        print("After function run")
        return result
    return wrapper
@decoration
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

print(add(10, 5))