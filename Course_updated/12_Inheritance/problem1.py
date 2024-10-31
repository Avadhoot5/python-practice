# 1. Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f'2-D Vector is: {self.i}i + {self.j}j')

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f'3-D Vector is: {self.i}i + {self.j}j + {self.k}k')

a = TwoDVector(3,6)
a.show()

b = ThreeDVector(3, 5, 9)
b.show()
