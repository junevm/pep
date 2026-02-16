def simple_gen():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    yield 3

g = simple_gen()
print(next(g))  # Output: Start \n 1
print(next(g))  # Output: Middle \n 2
print(next(g))  # Output: End \n 3
