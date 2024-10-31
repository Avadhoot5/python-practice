# Guess the number game.

import random
n = random.randint(1, 100)
a = -1
guess = 0

while (a != n):
    guess += 1
    a = int(input('Choose a number from 1 to 100: '))
    if (a < n):
        print('Enter higher number please')
    else:
        print('Enter lower number please')

print(f'You have guessed the correct number {n} in {guess} attemps!')
