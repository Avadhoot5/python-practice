class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f'The class attribute of a is: {cls.a}')


o = Employee()
o.a = 23 # instance attribute takes preference over class attributes
o.show()

