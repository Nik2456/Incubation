import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱ Function '{func.__name__}' executed in {duration:.4f} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function():
    time.sleep(5)
    print("Finished work!")

@timing_decorator
def add(a, b):
    return a + b

slow_function()
print(add(30, 20))
