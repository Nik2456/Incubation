def decorator(func):
    def wrapper():
        print("Transaction in initiate")
        func()
        print("Transaction done")
    return wrapper()

@decorator
def hello():
    print("Transaction is on going")

hello
