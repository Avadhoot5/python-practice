
# readline - reads 1 line after another, every line is read depending upon the number of times the readline function is called

with open('readfile.txt', 'r') as fs:

    # line1 = fs.readline()
    # print(line1)
    # line2 = fs.readline()
    # print( line2)
    
    # calling the fn using while loop
    line = fs.readline()
    while (line != ''):
        print(line)
        line = fs.readline()



# readlines - reads all the lines of the file, and returns them in a form of list

with open('readfile.txt', 'r') as fs:
    lineList = fs.readlines()
    print(lineList)

