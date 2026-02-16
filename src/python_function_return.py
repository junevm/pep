def calculate(a,b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

# sm, mul = calculate(10, 5) # valueError: too many values to unpack (expected 2)
sm, diff,prod = calculate(10, 5) 
print("Sum:", sm)
print("Difference:", diff)
print("Product:", prod)  

def test():
    return 10
    return 20 # unreachable code

print(test) # function object
print(test()) # calling the function