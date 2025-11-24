def general_decorator(func):

    def wrapper():
        print("Before function run")
        func()
        print("After function run")
    return wrapper

@general_decorator
def say_hello():
    print("Hello!")
say_hello()
