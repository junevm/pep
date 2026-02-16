import json

d = {}

# populate dictionary from user input
while True:
    key = input("Enter key (or 'exit' to finish): ")
    if key.lower() == 'exit':
        break
    value = input("Enter value: ")
    d[key] = value


# dump dictionary to a JSON file
with open('output.json', 'w') as f:
    json.dump(d,f)