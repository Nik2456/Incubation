def add_numbers(*args):
    return sum(args)
print("Sum of all numbers=",add_numbers(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")
