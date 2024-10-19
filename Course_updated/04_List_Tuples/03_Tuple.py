tupEmpty = ()

print(type(tupEmpty))

tupSingle = (23,) #if (23) is written - this evaluates to int
print(type(tupSingle))

tupList = (23, 234, 'Apple', 'Orange', 5, 23.13, False, 23, 92)

# Tuple methods

count = tupList.count(23)
print('Count is:', count)

indexCheck = tupList.index(5)
print(indexCheck)

print(23 in tupList)

# length len(tupList)
# min and max 

# Slicing in tuple 
newTup = tupList[1:5]
print(newTup)

# unpacking in tuple 

myTuple = (1, 2, 3)
a, b, c = myTuple
print(a, b, c)
