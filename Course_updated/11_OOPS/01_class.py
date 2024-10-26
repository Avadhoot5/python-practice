class Employee :
    language = 'Py'
    salary = 1000000

# here name is object/instance attribute. salary and language are class attributes.

employee1 = Employee()
employee1.name = 'firstname' #object/instance attribute
print(employee1.name)
print(employee1.language)

newEmp = Employee()
newEmp.name = 'secondName'
print(newEmp.name)
print(newEmp.salary)
print(newEmp.language)



