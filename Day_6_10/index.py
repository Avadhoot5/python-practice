# Variables and Data Types 

a = 1
print(a)
b = "Hello"
print(b)

c = None
d = True
e = complex(3,1)
print(e)
print("The type of c is:", type(c))
print("The type of d is:",type(d))
print("The type of d is:",type(e))

# Exercise 1: Calculator using Python 

#operators in python
# 1. Arithmetic operators
'''
print(15+7)
print(6-2)
print(3*2)
print(3**3)
print(7/3)
print(7%5)
print(8//3)
'''

# Develop a calculator of performing add,sub,multi,divide,modulo,floor div. And provide output in a readable manner.

a = int(input("Enter first number to perform arithmetic operations: "))
b = int(input("Enter second number to perform arithmetic operations: "))
add = a+b
sub = a-b
multiply = a*b
divide = a/b
power = a**b
remainder = a%b
floordiv = a//b
print("Addition of",a,"and",b,"is:",add)
print("Subtraction of",a,"and",b,"is:",sub)
print("Multiplication of",a,"and",b,"is:",multiply)
print("Division of",a,"and",b,"is:",divide)
print("Power of",a,"to",b,"is:",power)
print("Remainder of",a,"when divided by",b,"is:",remainder)
print("Integer Division for",a,"and",b,"is:",floordiv)

# Typecasting in Python

# Two types of typecasting - Explicit & Implicit

# Explicit Typecasting

string = "23"
number = 7
string_number = int(string)
sum = string_number + number
print("The sum of both the number is", sum)

# Implicit Typecasting
# python converts lower level data type to a higher level data type, for preventing data loss

a = 2.3
b = 4
print(a+b)

# Taking User Input in Python

a = input("Enter first number: ")
b = input("Enter second number: ")
print("Without Typecaste",a+b)

c = int(a)
d = int(b)
print("With Typecaste",c+d)

# Also the value you pass to the variable must be of the same data type as declared in the program.
# If the value is passed as another data type, it throws an error.