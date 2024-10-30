class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f'The class attribute of a is: {cls.a}')

    # The implementation is hidden from the user - Abstraction
    @property
    def name(self):
        return f'{self.fname} {self.lname}'

    @name.setter
    def name(self, value):
        self.fname = value.split(' ')[0]
        self.lname = value.split(' ')[1]

# all above implementation is encapsulated - Encapsulation
o = Employee()
o.a = 23 # instance attribute takes preference over class attributes
o.show()

o.name = "Test world"
print(o.name)

