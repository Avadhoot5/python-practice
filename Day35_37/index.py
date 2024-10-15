# Exception Handling

# a = (input("enter a number:"))
# print(f"Multiplication table of {a} is")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i}: {int(a)*i}")
# except Exception as e:
#     print(e)

# print("Remaining lines of code")


try:
    num = int(input("Enter any integer value:"))
    a = [2,52,215,25]
    print(a[num])
except IndexError:
    print("index error occurred")
except ValueError:
    print("Number is not an integer:")

print("Remaining lines of code")

# Day 37 

# Finally keyword

# The reason we use finally is, when we are returning something in a function, and if we
# just print the values, that line is not executed, adding finally makes sure that the 
#  specific lines are executed.

# try:
#     l = [1,5,15,14]
#     i = int(input("enter a index: "))
#     print(l[i])
# except:
#     print("some error has occurred")
# finally:
#     print("This gets executed no matter what")

def fun():    
    try:
        l = [1,5,15,14]
        i = int(input("enter a index: "))
        print(l[i])
        return 1
    except:
        print("some error has occurred")
        return 0
    finally:
        print("This gets executed no matter what")

print(fun())