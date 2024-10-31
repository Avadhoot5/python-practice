l = [1,2,3,4,5,10]

for index, item in enumerate(l):
    print(f'The number at index {index} is {item}')

# list comprehensions

myList = [1,2,3,5,2,235,24]

squaredList = [i * i for i in myList]

print(squaredList)
