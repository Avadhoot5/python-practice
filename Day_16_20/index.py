# Match Case Statements

# import os 
# print("hello world..")
# os.system("python --version")

# While 

# x = int(input("Enter the value of x: "))
# match x:
#     case 0:
#         print("x is zero")
#     case 4 if x%2==0:
#         print("x%2 == 0 and case is 4")
#     case _ if x<10:
#         print("x is less than 10")

# num = int(input("enter a valid number: "))

# if(num==0):
#     print("The Number is Zero")
# elif(num<0):
#     print("The Number is Negative")
# elif(num>0):
#     print("The Number is Valid")


# num = int(input("enter a valid number: "))

# match num:
#     case 0:
#         print("The Number is Zero")
#     case 1 if (num<0):      # Negative not getting executed
#         print("The Number is Negative")
#     case 2 if (num>0):
#         print("The Number is Valid")
#     case _ if num!=0:
#         print("Please enter a valid number")



num = int(input("enter a valid number: "))

match num:
    case n if (n==0):
        print("The Number is Zero")
    case n if (num<0):
        print("The Number is Negative")
    case n if num>0:
        print("The Number is Valid")
    case _ if num!=0:
        print("Please enter a valid number")


# For Loops

# Sometimes, a programmer wants to execute a group of statements a certain number of times.

name  = "Avadhoot"
for i in name:
    print(i)

# Iterating over a list
#nesting for inside a for loop

colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# Range in python

for k in range(10):
    print(k)

for k in range(3,11):
    print(k+1)

for k in range(3,12,2):
    print(k)

# multiplying a number

num = int(input("Enter a number to Multiply: "))
for i in range(1,11):
    print(i*num)

# decrementing the values

for i in range(10,1,-1):
    print(i)


# While Loops

# i = 0
# while(i<5):
#     print(i)
#     i = i + 1


# Emulate Do while loop in python

i = int(input("Enter a number: "))
print(i)
while(i<=10):
    i = int(input("Enter a number: "))
    print(i)
else:
    print("Done With the Code!")


# decrementing the values

count = 5
while(count>0):
    print(count)
    count = count-1

# Emulate Do while loop in python
# python itself does not support do while loop, so we make while condition true and run it to infinite
# and add a if condition with a break, so the entire loop gets break.

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break

# Break

# for i in range(12):
#     if(i==10):
#         break
#     print("5 X",i,"=",5*i)
# print("Done with the loop")

# for i in range(11):
#     if(i==10):
#         break
#     print("4 X", i,"=", 4*i)


# for i in range(12):
#     if(i==10):
#         print("Skipping the 10th Iteration")
#         continue
#     print("5 X",i,"=",5*i)
# print("Done with the loop")


for i in range(1,101,1):
    print(i, end=" ")
    if(i==50):
        break
    else:
        print("Molololo")
print("Thank You")

        
# Continue

# for i in [2,3,4,6,8,0]:
#     if(i%2!=0):
#         continue
#     print(i)

# Functions

# example

# a = input
# b = input
# mean1 = (a*b)/(a+b)
# print(mean1)

# c = input
# d = input
# mean2 = (c*d)/(c+d)
# print(mean2)

# repeating the code on and on for performing one task does not makes sense, so we use FUNCTIONS

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
def Gmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    greater(a, b)

def greater(a, b):
    if a==b:
        print("both are equal")
    elif a>b:
        print(a, "is greater")
    else:
        print(b, "is greater")

Gmean(a, b) # calling a function

# if you want to complete a function later, but just needs to be added in the code use PASS

def testfun(a, b):
    pass


