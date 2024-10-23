# 1. open poems.txt and find out word 'twinkle'

# with open('problem/poems.txt', 'r') as fs:
#     readList = fs.read()
#     findWord = readList.find('twinkle')
#     if (findWord != -1):
#         print('Word Found')
#     else:
#         print('word not found')

# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random

def game():
    print('You are playing the game....')
    score = random.randint(1, 100)
    print(f'Your score is: {score}')
    with open('problem/highscore.txt') as fs:
        highScore = fs.read()
        if (highScore != ''):
            highScore = int(highScore)
        else:
            highScore = 0

    if (score > highScore):
        with open('problem/highscore.txt', 'w') as fs:
            fs.write(str(score))

    return score

# game()

# 3. generate multiplication tables from 2 to 20 and write it to the different files. place these files in a folder for a 13-year old

def mulTable(n):
    table = ''
    for i in range(1, 11):
        table += f'{n} X {i} = {n * i} \n'
    return table

def createFiles():
    for i in range(2, 21):
        value = mulTable(i)
        with open(f'problem/tables/Table_{i}', 'w') as fs:
            fs.write(str(value))

# createFiles()

# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

# word = 'Donkey'

# with open('problem/fileWord.txt', 'r') as fs:
#     content = fs.read()

# contentUpdated = content.replace(word, '#####')

# with open('problem/fileWord.txt', 'w') as fs:
#     fs.write(contentUpdated)

# 5. Repeat program 4 for a list of such words to be censored.

# wordList = ['donkey', 'monkey', 'bad', 'money']

# with open('problem/listWords.txt', 'r') as fs:
#     content = fs.read()

# for word in wordList:
#     content = content.replace(word, '#' * len(word))

# with open('problem/listWords.txt', 'w') as fs:
#     fs.write(content)

# 6. mine a log file and find out whether it contains ‘python’.

# with open(f'problem/log.txt') as fs:
#     content = fs.read()

# if ('python' in content):
#     print('Yes python is present')
# else:
#     print('Not present')


# 7. find out line number

# with open(f'problem/log.txt') as fs:
#     lines = fs.readlines()

# lineNo = 1
# for line in lines:
#     if ('python' in line):
#         print(f'Yes python is present on line: {lineNo}')
#         break
#     lineNo += 1
# else:
#     print('No python is not present')


# 8. make a copy of a text file

# with open('problem/this.txt') as fs:
#     content = fs.read()

# with open('problem/copyOfThis.txt', 'w') as fs:
#     fs.write(content)

# 9. find out file is identical & matches content of another file

# with open('problem/this.txt') as fs:
#     fileContent1 = fs.read()

# with open('problem/copyOfThis.txt') as fs:
#     fileContent2 = fs.read()

# if (fileContent1 == fileContent2):
#     print('Yes files are identical')
# else:
#     print('Not identical')

# 10. wipe out content of a file.

# with open('problem/clearMe.txt', 'w') as fs:
#     fs.write('')

# 11. rename a file 
# import os

# os.rename('problem/clearMe.txt', 'problem/clearFile_by_python.txt')

