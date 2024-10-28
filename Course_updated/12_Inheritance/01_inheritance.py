class Employee:
    company = 'ITC'
    name = 'test'
    def show(self):
        print(f'The name of the employee is {self.name} and the company is {self.company}')

class Programmer(Employee):
    company = 'ITC Infotech'
    language = 'python'
    def showLanguage(self):
        print(f'The company is {self.company} and he is good with {self.language}')


obj = Programmer()

obj.show()
obj.showLanguage()

