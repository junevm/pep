def fizz_buzz(n):
    for i in range(1, n + 1):
        # why only check this first? Because numbers divisible by both 3 and 5 should print "FizzBuzz" first. If we check for 3 or 5 first, we would miss those cases.
        if i % 3 == 0 and i % 5 == 0:  
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    

fizz_buzz(15)