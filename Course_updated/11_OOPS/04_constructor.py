class Employee:

    def __init__(self, name, salary, language): # dunder method, which is automatically called
        print('I"m creating an object')
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")

    @staticmethod
    def greet():
        print('Good morning')


test = Employee('firstName', 1200000, 'Javascript')

print(test.name, test.salary, test.language)


