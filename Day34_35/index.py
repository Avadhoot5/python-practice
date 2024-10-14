# Dictionary Methods

ep = {
    122: 45,
    123: 52,
    352: 52,
    252: 26
}
ep2 = {355:624, 626:252}
ep.update(ep2)
print(ep)

# counting the number of values in a dictionary

# print(len(ep))
# val = ep.keys()
# print(len(val))

# clear the items of a dictionary

# ep.clear()
# print(ep)

empt = {}
print(type(empt))
print(empt)

# pop() - removes the key value pair whose key is passed as the parameter

ep.pop(123)
print(ep)

# popitem() - removes the last k-v pair 

popcatch = ep.popitem()
print(ep)
print(popcatch)

# del - used to delete the dictionary

deleting = {1:3,3:1}

del deleting[1] # used to delete the item using particular key

# del deleting
# deleting.clear()

print(deleting)

# for Loop with else
# IMPORTANT: else block will only be executed when for/while loop is succesfully executed for all values.
# else executes when loop ends, not when loop breaks.

for i in range(5):
    print(i)
else:
    print("the loop has ended")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("The loop is broken")

i = 0
while i<5:
    print(i)
    i = i+1
    if i>3:
        break
else:
    print("while loop is done")

