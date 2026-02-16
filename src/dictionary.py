d = [
    {"id":1, "name":"Alice","marks":87,"city":"New York"},
    {"id":2, "name":"Bob","marks":92,"city":"Los Angeles"},
    {"id":3, "name":"Charlie","marks":78,"city":"Chicago"},
    {"id":4, "name":"David","marks":85,"city":"Houston"},
    {"id":5, "name":"Eve","marks":90,"city":"Phoenix"}

]


print("all students:\n")
for entry in d:
    print(f"ID: {entry['id']}, Name: {entry['name']}, Marks: {entry['marks']}, City: {entry['city']}")
print("\n")

print("filtered students:\n")
for entry in d:
    if entry["marks"]>80:
        print(f"ID: {entry['id']}, Name: {entry['name']}, Marks: {entry['marks']}, City: {entry['city']}")
print("\n")


print("grace marks updated:\n")
for i,v in enumerate(d):
    marks = v["marks"]+5
    if not marks>100:
        d[i]["marks"] = marks

print(d)
        

print("sort students by marks:\n")

sorted_list = sorted(d, key=lambda x: x["marks"])
for student in sorted_list:
    print(student)

