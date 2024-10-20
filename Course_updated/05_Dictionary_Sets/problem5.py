# 1. create a dict of hindi words with values as their english translations.

dictWords =  {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "सुख": "Happiness",
    "प्यार": "Love",
    "दोस्त": "Friend",
    "घर": "Home",
    "सूर्य": "Sun"
}

# for i in dictWords:
#     print(f'Hindi word {i} = {dictWords[i]}')

# 2. input 8 nos from the user and dispay all unique no's.

numbers = set()

# for i in range(8):
#     number = int(input(f'Enter Number {i+1}: '))
#     numbers.add(number)

print(numbers)

# 3. can we have a set with 18(int) and '18' (str) as a value in it.

setValue = {18, '18'}
print(setValue, len(setValue))

# 4. length of the set => 
s = set()

s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))

# 5. s = {}
dict = {}
print(type(dict))

# 6. empty dict. Allow 4 friends to enter their fav language as value and use keys as their names. assume names are unique

friendList = {}

# for i in range(4):
#     name = input((f'Enter name friend {i+1}: '))
#     favLang = input('Enter your favourite language: ')
#     friendList[name] = favLang

print(friendList)

# 7. if 2 names are same, what will happen to problem 6
# Ans - if 2 names are same, the language added in the last will be the value for that key

# 8. if 2 friends languages are same, what will happen to problem 6
# Ans - the dict will show same langauge for the 2 friends.
 
# 9. change values inside a list which is contained in set S.
s = {8, 7, 12, 'test', [1, 2]}

print(s)

# No we cannot change sets can only contain immutable (hashable) objects

