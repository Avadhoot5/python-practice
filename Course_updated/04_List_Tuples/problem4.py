# 1. store 7 fruits in a list entered by the user

fruitList = []
# i = 0

# while (i < 7):
#     fruit = input('Enter the fruit name: ')
#     fruitList.append(fruit)
#     i += 1

print(fruitList)

# 2. accept marks of 6 students and display them in a sorted manner

markList = []

# for i in range(1, 7):
#     marks = int(input(f'Enter your marks Student {i}: '))
#     markList.append(marks)

markList.sort()
print(markList)

# 3. check that type cannot be changed 

a = 23
print(type(a))

a = 'hello world'
print(type(a))


# 4. sum a list with 4 numbers

fourNum = [1,5,2,9]

print(sum(fourNum))

# 5. count no of 0's in tuple

a = (7, 0, 8, 0 , 0 , 9)

print(a.count(0))



