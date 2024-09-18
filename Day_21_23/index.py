# function arguments

# Default arguments

def avg(a=2, b=4):
    print("The average of two numbers is: ", (a+b)/2)
avg()

# values get override if pass arguments while calling the function. eg. avg(a=4,b=23) OR avg(2) only a is replaced. avg(b=4) b is replaced

# Keyword arguments, like passing the values in form of keys

avg(a=23,b=21)

# Required arguments

# in case if we don't pass arguments in Key value syntax, then it is neccesary to pass the arguments 

def req(a,b):
    print("sum of the two numbers is:", a+b)
req(3,5)

# Variable Length arguments

# *paramater = taken as TUPLE, **paramater = taken as DICTIONARY

def sum(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum + i
    return sum

sumas = sum(4,12,1,5,1,1231,21)
print(sumas)


# Introduction to Lists 

# marks = [1,5,2345,253]
# print(marks)
# print(type(marks))

# for i in marks:
#     if i<270:
#         print(i)
#     else:
#         print("condition not satisfied")

# print(marks[0 :2])

# listname[start:end:jump_index]

list1 = ["hello",3,1,7,8,2,5,21,36]
print(list1[1:7:2])
print(list1[1:8:3])

# Check whether an item is present in the list or not 

if 3 in list1:
    print("Yes exists!")
if 23 in list1:
    print("Yes exists!")
else:
    print("No doesn't exists")

# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:
# List = [Expression(item) for item in iterable if Condition]

list2 = [item for item in range(5)]
print(list2)

list3 = [item for item in range(11) if item%2==0]
print(list3)

list4 = [item*item for item in range(11) if item%2==0]
print(list4)


# List Methods

l = [14,34,25,235,1,2,2,1,251,243]
print(l)

# append method - used to add elements to the list 

# l.append(23)
# l.append(32)
# print(l)

# sort method - used to sort the list in the ascending order
# sort(reverse = True) - used to sort the list in descending order
# can't print the list while applying the methods, first apply the method and then print the list

# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# reverse method -  reverses the list

# l.reverse()
# print(l)

# index method - returns the value of the element present at the given index 

# print(l.index(34))

# # count method - prints the number of times an element occurs in the list

# print(l.count(1))

# copy method - used to copy the list 

# l1 = [23,52,35,252,1]
# print(l1)
# m = l1  #here same list is taken as a reference, as the list is stored in l1's memory location, so if we change anything l1 gets changed
# m[0] = 0
# print(l1)

# to avoid any changes in the orginal list, we use copy() method

l1 = [23,52,35,252,1]
print(l1)
m = l1.copy()  #here same list is taken as a reference, as the list is stored in l1's memory location, so if we change anything l1 gets changed
m[0] = 0
print(l1)
print(m)

# Insert Method - used to insert a value at a specific index.

l1.insert(0, 3123)
print(l1)

# extend method - used to open a list and add it in another list's end

l2 = [3,25,2]
m2 = [5,21,53]
l2.extend(m2)
print(l2)

# concatenate method - add two string

a = [23452,52,6,2625]
b = [53,16,262]
c = a+b
print(c)




