from functools import reduce

# 1.  WAP to input name, marks and phone numbers of student and format it liek below 
# The name of the student is {student}, his marks are {marks} and phone num is {phone}

# name = input('Enter your name: ')
# marks = int(input('Enter your marks: '))
# phoneNum = int(input('Enter your phone Number: '))

# print('The name of the student is {}, his marks are {} and phone num is {}'.format(name, marks, phoneNum))

# 2. List containing the mul table of 7. convert it to vertical string of same numbers.

table = [str(7 * i) for i in range(1, 11)]

s = '\n'.join(table)
# print(s)

# 3. filter a list of numbers which are divisible by 5.

numbers = [4,24,55,25,95,21,90,70,82]

filt = lambda x: x%5 == 0

numbers_divisible_by5 = filter(filt, numbers)
# print(list(numbers_divisible_by5))

# 4. find the maximum of numbers in a list using reduce fn.

def maxNum(a, b):
    if (a > b):
        return a
    elif (b > a):
        return b
    else:
        return
    
maxNumber = reduce(maxNum, numbers)
# print(maxNumber)

# 5. pip freeze for the system interpreter. take contents and create similar env.

# DONE

# 6. explore flask module and create a web server using flask and python.


