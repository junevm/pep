arr = [1,2, 3 ,4 ,5, 'A', 'B', 'C', 6, 7, 8, 9, 10, 'D', 'E', 'F']
even_sum = 0
odd_sum = 0
for i in arr:
    if type(i)==type(0):
        if i%2==0:
            even_sum += i
        else:
            odd_sum += i

print(f'sum even: {even_sum}')
print(f'sum odd: {odd_sum}')