# saving the table in a file
n = int(input('Enter a number: '))

mulTable = [n * i for i in range(1,11)]
print(mulTable)

with open('Tables.txt', 'w') as f:
    for i in mulTable:
        f.write(str(i) + '\n')
