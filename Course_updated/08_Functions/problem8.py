# 1. functions to find greatest of 3 nos.

# numList = []

# for i in range(3):
#     n = int(input(f'Enter number {i+1}: '))
#     numList.append(n)

# maxNum = 0
# for i in numList:
#     if i > maxNum:
#         maxNum = i

# print(f'Greatest number of 3 is: {maxNum}')

# 2. convert celsius to FH

def temp(n):
    fH = (32)+((9/5)*n)
    return fH

print(temp(5))

# 3. prevent python print() function to print a new line at the end

def printPrevent():
    print('hello', end=' ')
    print('world', end='')

# printPrevent()

# 4. recursive function to calculate the sum of first n natural numbers.

def sumFn(n):
    if n == 1:
        return 1
    else:
        return n + sumFn(n-1)

# print(sumFn(10))

# 5. print first n lines start pattern upside down

def pattern(n):
    for i in range(0, n):
        print('*' * (n-i), end = '')
        print('')

# pattern(4)

# 6. convert inches to cms

def inchToCm(n):
    return (n*2.54)

answer = inchToCm(5)
# print(answer)

# 7. function to remove a given word from a list and strip it at the same time.

names = ["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Isaac","Jasmine"]

def removeWord(arr, word):
    newArr = []
    for i in names:
        if (i != word):
            newArr.append(i)
    return newArr

ans = removeWord(names, 'Bob')
print(ans)


# 8. function to print table of a number

def table(n, i):
    if i == 11:
        return 1
    else:
        print(n * i)
        table(n, i+1)


# table(5, 1)

