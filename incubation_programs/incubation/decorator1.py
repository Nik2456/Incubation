def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Error: Cannot divide by zero!")
            return
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)  # 5.0
divide(10, 0)  # Error: Cannot divide by zero!
