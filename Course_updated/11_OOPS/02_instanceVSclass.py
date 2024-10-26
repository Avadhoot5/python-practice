# Instance V/S class attributes

class Employee:
    language = 'Python'
    salary = 120000

test = Employee()
test.language = 'Javascript' #here instance takes precendence over class attribute

print(test.language, test.salary)

