# self keyword

class Employee:
    language = 'Python'
    salary = 120000

# TypeError: Employee.getInfo() takes 0 positional arguments but 1 was given
    # def getInfo():
    #print(f"The language is {language}, and the salary is {salary}")
    
    def getInfo(self):
        print(f"The language is {self.language}, and the salary is {self.salary}")


test = Employee()
test.language = 'javascript'

test.getInfo()
# the above is equivalent to Employee.getInfo(test)

