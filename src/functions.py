def maxnum(a, b):
    if a > b:
        return a
    else:
        return b
    
# print(maxnum(10, 20))

a = [1,324,43,2,235,23432,4,324,324]
m = float('-inf')
for i in a:
    m = maxnum(m,i)
print(m)

# second largest number
first = float('-inf')
second = float('-inf')
for num in a:
    if num>first:
        second = first
        first = num
    elif num>second and num!=first:
        second = num

print(second if second!=float('-inf') else "No second largest")
