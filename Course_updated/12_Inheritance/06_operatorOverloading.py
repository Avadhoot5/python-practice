class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
    def __mul__(self, num):
        return self.n * num.n

n = Number(1)
m = Number(2)

# print(m + n) throws an error, 

print(m + n)
print(m * n)


