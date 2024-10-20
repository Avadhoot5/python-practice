mySet = {1, 2, 3, "apple", "banana", "cherry"}

print(mySet, type(mySet))

# methods. 

# add - adds an element in the set
mySet.add(5)
print(mySet, type(mySet))

# remove - removes an element from the set
mySet.remove(5)
print(mySet, type(mySet))

# pop - remove and return an arbitrary element from the set

popElement = mySet.pop()
print(f'popped element is {popElement}')

# clear - clears the entire set
# mySet.clear()
# print(mySet, type(mySet))

# lenght of the set 
print(f'Length of set is: {len(mySet)}')

