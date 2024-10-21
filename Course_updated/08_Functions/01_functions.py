# Functions in python

def fun1():
    print('hello')

# fun1()

def avg(a,b,c):
    return int((a+b+c)/3)

ans = avg(2,34,4)
# print(ans)



def rec(n):
    # base condition
    if n == 0:
        return
    # hypothesis
    rec(n-1) # induction 
    print(n)     

# rec(10)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

factAns = factorial(0)
print(factAns)
