import time


def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}(): {(end_time - start_time) * 1000}ms")
        return result
    return wrapper

@log_execution
def add_numbers(a, b):
    print(f"sum: {a + b}")



@log_execution
def multiply_numbers(a, b):
    print(f"product: {a * b}")


add_numbers(5, 10)
multiply_numbers(5, 10)
    


