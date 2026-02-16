from collections import defaultdict

d = {'a': 1, 'b': 2, 'c': 1, 'd': 1}

inverted_dict = defaultdict(list)

for key, value in d.items():
    # if value not in inverted_dict:
    #     inverted_dict[value] = []
    inverted_dict[value].append(key)

print(dict(inverted_dict))
