# oneLadder = 1 step. Method = 1

# twoLadder = [1, 1] / [2]. Method = 2 

# 6th ladder = 
# 5th + 4th
# 4th 3rd + 3rd  2nd
# 3rd 2nd 2nd 1st + 2nd 1st 1st
# 2nd 1st 1st 0 + 1st 0 0 



# X power n 

# 2 power 4  -> fn(x, n) => fn(constant, numberof times). 

# def power(x, n):
#     if (n == 0):
#         return 1
#     xn = power(x, n//2) * power(x, n//2)
#     if (n % 2 == 0):
#         return xn
#     else:
#         return x * xn


# ans = power(2, 10)
# print(ans)

# def toh(n, id1, id2, id3):
#     if (n == 0):
#         return 1
#     toh(n-1, id1, id3, id2) # move 2 discs recursively from A to C help of B
#     print(f'{n} [{id1} -> {id2}]')
#     toh(n-1, id3, id2, id1)

# answer = toh(3, 'A', 'B', 'C')
# print(answer)

# arr = []
# for i in range(1, 11):
#     arr.append(i)

# def printArr(arr, i):
#     # faith index = 0. will print 0 to n-1
#     # expectation. index = 1. print 1 to n-1
#     # faith_exp. print(arr[currentIndex]). fn(i+1). i == arr.length return

#     if (i == len(arr)):
#         return
#     print(arr[i])
#     printArr(arr, i+1)

# printArr(arr, 0)

# operator overloading

class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self, num):
        return self.n + num.n
    
    def __mul__(self, num):
        return self.n * num.n

# a = Number(1)
# b = Number(2)

# print(a+b)
# print(a*b)
