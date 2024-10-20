# 1. find the greatest of 4 nos entered by user

listNum = []

# for i in range(4):
#     listNum.append(int(input(f'Enter number {i+1}: ')))

# print(max(listNum))

# 2. find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. assume 3 subjects.

marksList = []

# for i in range(3):
#     mark = int(input(f'Enter marks for subject {i+1}: '))
#     marksList.append(mark)

passingMark = False

counter = 0

if (sum(marksList) < 40):
    print('Failed')
else:
    for i in marksList:
        if (i < 33):
            counter+=1
    if (counter > 0):
        print('Failed')
    else:
        print('Passed')

# 3. detect spam messages

# spamList = ['make a lot of money', 'buy now', 'subscribe this', 'click this']

# userMessage = input('Spam detect message: ').lower()

# if (userMessage in spamList):
#     print('SPAM! message found')
# else:
#     print('Not spam')

# 4. find a given username contains less than 10 characters or not.

# userName = input('Enter your username: ').strip()

# if (len(userName) < 10):
#     print('Lenght is LESS than 10 characters')
# else:
#     print('Length GREATER than 10 characters')

# 5. find out whether a given name is present in a list or not.

# names = ["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Isaac","Jasmine"]

# nameInput = input('Enter your name to check in the list: ').capitalize()

# if (nameInput in names):
#     print('Your name is present')
# else: 
#     print('Name NOT present')

# 6. calculate grade of students based on his marks

markS = int(input('Enter your Total marks: '))

if (markS > 90 and markS <= 100):
    print('Ex')
elif (markS > 80 and markS <= 90):
    print('A')
elif (markS > 70 and markS <= 80):
    print('B')
elif (markS > 60 and markS <= 70):
    print('C')
elif (markS > 50 and markS <= 60):
    print('D')
elif (markS <= 50):
    print('F')

