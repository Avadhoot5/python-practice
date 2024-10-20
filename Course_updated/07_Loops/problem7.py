# 1. print multiply for a given number

# n = int(input("enter a number to display multiplication table: "))

# for i in range(1, 11):
#     print(i * n)

# 2. greet persons form the list, whose name starts with S

l = ['Harry', 'Soham', 'Sachin', 'Rahlul']

# for i in l:
#     if i.startswith('S'):
#         print(f'Hello, {i}')

# 3. problem 1 using while loop

# i = 1
# while (i < 11):
#     print(i * n)
#     i += 1

# 4. find if a number is prime or not.

# n = int(input('Enter a number to find if it is prime or not: '))

# isPrime = True

# if (n <= 1):
#     isPrime = False
# elif (n == 2):
#     isPrime = True
# else:
#     for i in range(2, int(n**(0.5)) + 1):
#         print(i)
#         if (n % i == 0):
#             isPrime = False
#             break

# if (isPrime):
#     print('Yes it is a prime number')
# else:      
#     print('Not a prime number')

# 5. find the sum of first n natural numbers using while loop

# n = int(input('Enter a number: '))

# i = 1
# sum = 0

# while (i < n+1):
#     sum += i
#     i += 1

# print(f'Sum of {n} natural number is: {sum}')

# 6. calculate the factorial of a given number using for loop. n!

# n = int(input('Enter a number: '))

# fact = 1

# for i in range(1, n+1):
#     fact *= i
#     i += 1

# print(f'Factorial of {n} is {fact}')

# 7. print pyramid for n 
# n = int(input('pyramid size ?: '))

# str = ''
# for i in range(0, n):
#     for k in range(0, (n-i)):
#         str += ' '
#     for j in range(1, (2*i) + 2):
#         str += '*'
#     str += '\n'

# print(str)

# 8. print left triangle for n 

# n = int(input('pyramid size ?: '))

# str = ''
# for i in range(1, n+1):
#         str += '*'
#         print(str)

# 9. print square pattern

n = int(input('pyramid size ?: '))

str = ''
for i in range(n):
    if (i == 0 or i == n-1):
        for j in range(n):
            str += '*'
    else:
        for j in range(n):
            if (j == 0 or j == n-1):
                str += '*'
            else:
                str += ' '
    str += '\n'

print(str)


# 10. print * table of n using for loops in reversed order

# n = int(input('Enter a number: '))

# for i in range(10, 0, -1):
#     print(n * i)

