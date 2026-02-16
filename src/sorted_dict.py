data = [{'id':2, 'name':'rishab_2'},
        {'id':1, 'name':'rishab_1'},
        {'id':3, 'name':'rishab_3'}
        ]

ids = []
sorted_data=[]

for item in data:
    ids.append(item['id'])

ids.sort()

for id in ids:
    # sorted_data.append(next(item for item in data if item.get('id') == id))

    for item in data:
        if item['id'] == id:
            sorted_data.append(item)
            break

print(sorted_data)

# alternate way
data.sort(key=lambda x: x['id'])