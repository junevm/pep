def decorator_1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1: Before calling", *args, **kwargs)
        result = func(*args, **kwargs)
        print("Decorator 1: After calling", *args, **kwargs)
        return result
    return wrapper

@decorator_1
def add_numbers(a, b):
    return a + b


@decorator_1
def multiply_numbers(a, b):
    return a * b

if __name__ == "__main__":
    sum_result = add_numbers(5, 10)
    print("Sum Result:", sum_result)

    product_result = multiply_numbers(5, 10)
    print("Product Result:", product_result)

