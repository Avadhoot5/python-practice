class Employee:
    def __init__(self):
        print('I am Employee constructor')
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print('I am Programmer constructor')
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print('I am Manager constructor')
    c = 3

# o = Employee()
# o = Programmer()
# o = Manager()

# If we need to call the parent constructor just use super() keyword.

o = Manager()
