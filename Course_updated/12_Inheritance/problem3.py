# Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:

    @property


    def increment(self):
        newSalary = self.salary * (0.15)
        print(f'The increment to your salary is 15% = {newSalary}')

a = Employee(1000000)

a.increment()
