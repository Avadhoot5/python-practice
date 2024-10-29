# Multiple inheritance

class Employee:
    company = 'ITC'
    name = 'Default name'
    def show(self):
        print(f'The name of the employee is {self.name} and the company is {self.company}')

class Coder:
    language = 'python'
    def printLanguages(self):
        print(f'out of all languages here is your language: {self.language}')

class Programmer(Employee, Coder):
    company = 'ITC Infotech'
    def showLanguage(self):
        print(f'The company is {self.company} and he is good with {self.language}')

a = Employee()
b = Coder()
c = Programmer()

a.show()
b.printLanguages()

c.show()
c.printLanguages()
c.showLanguage()

# Multilevel inheritance



