name = 'hello world'

print(name[0]) # printing value based on index

# Index in strings

print(name[0:3]) # 0 to 2. 3 is not included

print(name[1:]) # from 1 index to the lenght of the string

print(name[:4]) # start form 0 index

# Negative indexing

print(name[-4: -1]) #simply convert this to +ve index => len() - -ve index.

# print(name[11-4: 11-1])
# print(name[7: 10])

# Slicing with skip value

a = '123456789'

# Start_index, end_index - 1, skip_value
print(a[0:9:2])



