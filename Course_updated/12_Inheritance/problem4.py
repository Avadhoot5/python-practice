# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
    
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imaginary_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imaginary_part)

    def __str__(self):
        return f'{self.r} + {self.i}i'

a = Complex(2,6)
b = Complex(5, 9)

print(a + b)
print(a * b)


