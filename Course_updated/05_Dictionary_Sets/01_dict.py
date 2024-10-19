# Dict is a collection of key value pairs

# Properties
# Unordered collection of different data types, Mutable, Indexed, cannot contain duplicate keys 

marks = {
    'Student1': 100,
    'Student2': 80,
    'Student3': 90,
}

print(marks, type(marks))

for i in marks:
    print(f'{i} has secured {marks[i]} marks')

