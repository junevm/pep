arr = [[0,1,2],[3, 4, 5],[6, 7, 8],[9,10,11,12,13],[14,15,16,17],[2]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if j%2==0:
            arr[i][j] *=10

print(arr)
    

