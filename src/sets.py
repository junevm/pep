# find missing element
a = {1,2,3,4,5}
b = {2,3,1,5}
c = a - b
print(c)


# find first repeating element
c = set()
arr = [3,5,3,1,4,5,2]
for i in arr:
    if i in c:
        print(i)
        break
    c.add(i)
    
    
    



