l = [123,132,5,3,52,13,62,2346,2,235,2352]

# using enumerate

for index, item in enumerate(l):
    if (index == 2 or index == 4 or index == 6):
        print(item)

# list comprehension to print a list 

n = int(input('Enter a number: '))

mulTable = [n * i for i in range(1,11)]
print(mulTable)

