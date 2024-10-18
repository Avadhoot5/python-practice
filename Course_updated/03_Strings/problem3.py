# 1. display a user entered name by GA using input()

# userInput = input('Enter your name: ')
# print(userInput, 'Good Afternoon')

# 2. fill in a letter template with name and date
import datetime

name = input('Enter your name: ')
date = datetime.datetime.now()

letter = '''
        Dear <|Name|>,
        You are selected!
        <|Date|>
'''

print(letter.replace('<|Name|>', name).replace('<|Date|>', str(date).split(' ')[0]))

# 3. detect double spaces

string = 'hello  this is a  test  message'
# string = 'hello this is a test message'

print(string.find('  '))

# 4. replace double space with single space

stringReplace = 'hello  this is a  test  message'
print(stringReplace.replace('  ', ' '))

# 5. format th ltter using escape sequence

Letter = 'Dear Test,\n\tthis is a course.\n Thanks!'
print(Letter)

