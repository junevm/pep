arr = [3,4,5,6,7,-4,-3,-2]
n = len(arr)
res=set()
for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[i]+arr[j]+arr[k]==0:
                res.add(tuple(sorted([arr[i],arr[j],arr[k]])))
                

print(res)


arr.sort()
n = len(arr)
res = set()
for i in range(n):
    left = i + 1
    right = n - 1
    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]
        if current_sum == 0:
            res.add((arr[i], arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            right -= 1
print(res)