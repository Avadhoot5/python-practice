'''
1 for snake
-1 for water
0 for gun
'''

import random

computerValue = random.choice([1, -1, 0])

dict = {
    's': 1,
    'w': -1,
    'g': 0
}

userInput = input('Enter your choice (s, w, g): ')
userValue = dict.get(userInput)

reverseDict = {
    1: 'Snake',
    -1: 'Water',
    0: 'Gun'
}

# display values
print(f'You choose: {reverseDict[userValue]}')
print(f'Computer choose: {reverseDict[computerValue]}')

# bruteforce comparison

# if (userValue == computerValue):
#     print('It is a draw!')
# else:
#     if (userValue == 1 and computerValue == -1):
#         print('You Win')
#     elif (userValue == 1 and computerValue == 0):
#         print('You lose')
#     elif (userValue == -1 and computerValue == 1):
#         print('You lose')
#     elif (userValue == -1 and computerValue == 0):
#         print('You Win')
#     elif (userValue == 0 and computerValue == -1):
#         print('You lose')
#     elif (userValue == 0 and computerValue == 1):
#         print('You Win')
#     else:
#         print('Something went wrong')

# better approach using finding pattern

if (userValue == computerValue):
    print('It is a draw!')
else:
    if ((userValue - computerValue) == 2 or (userValue - computerValue) == -1):
        print('You Win')
    elif ((userValue - computerValue) == -2 or (userValue - computerValue) == 1):
        print('You Lose')
    else:
        print('Something went wrong')
