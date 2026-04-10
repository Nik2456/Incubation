def decorator(func):
    def wrapper():
        print("Transaction in initiate")
        func()
        print("Transaction done")
    return wrapper()

@decorator
def hello():
    print("Transaction is on going")

arr = [1, 2, 3, 4, 5]

if 4 in arr:
    print("Found")