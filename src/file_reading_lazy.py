def readfile():
    with open('src/sample.txt','r') as f:
        for line in f:
            yield line.strip()

line = readfile()
print(next(line))  
print(next(line))  
print(next(line))  
print(next(line))  
print(next(line))  

