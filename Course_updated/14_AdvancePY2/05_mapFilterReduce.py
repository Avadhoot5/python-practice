from functools import reduce

# Map Fn

l = [1,3,5,9,2,6]

sqaure = lambda x : x * x

sqList = map(sqaure, l)

# convert the object into List
print(list(sqList))

# Filter Fn

def even(n):
    if (n % 2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

# Reduce Fn

def total(a, b):
    return a + b

reducedList = reduce(total, l)
print(reducedList)

