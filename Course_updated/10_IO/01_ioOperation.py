
# here we need to close the file always.

# fs = open('readfile.txt')
# readFile = fs.read()
# print(readFile)

# fs.close()

# Alternate - we can use with keyword

with open('readfile.txt', 'r') as fs:
    readFile = fs.read()
    print(readFile)

# writing to a file 

with open('write.txt', 'w') as fs:
    content = '''
    This is a content which is getting written to a file
    '''
    fs.write(content)

