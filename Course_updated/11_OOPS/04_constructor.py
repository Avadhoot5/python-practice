class Employee:
    language = 'Python'
    salary = 120000

    def __init__(self):
        print('I"m creating an object')

    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")

    @staticmethod
    def greet():
        print('Good morning')


test = Employee()
test.name = 'firstName'
test.language = 'javascript'

print(test.name, test.salary)

