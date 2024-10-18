upperCase = 'hello'
print(upperCase.upper())

lowerCase = 'HELLO WORLD'
print(lowerCase.lower())

cap = 'this is a text'
print(cap.capitalize())

titleEg = 'this is an example of title in a blog'
print(titleEg.title())

stripEg = ' hello  world  '
print(stripEg.strip())

stringSplit = 'hello how are you'
print(stringSplit.split())

stringJoin = ['this', 'is', 'a', 'join', 'example']
print('-'.join(stringJoin))

replaceStr = "hello world is world"
print(replaceStr.replace("world", "Python"))

textFind = 'hello world'
print(textFind.find('w')) # index of the word 

textCount = 'hello count the hello'
print(textCount.count('hello'))

text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.endswith("world")) 

text = "12345"
print(text.isdigit())

text = "hello"
print('Is alpha', text.isalpha())

# Returns True if all characters in the string are alphanumeric (letters or numbers).
text = "hello234"
print(text.isalnum()) 

