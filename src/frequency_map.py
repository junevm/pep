# return a dict containing highest frequency items only
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,5,5,5,5]

d = {}

for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

max_value = max(d.values())

filtered = {k:v for k,v in d.items() if v==max_value}

print(filtered)

