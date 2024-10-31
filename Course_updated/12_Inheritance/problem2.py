# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’

class Animals:
    def __init__(self, animalType):
        self.animalType = animalType
    
    def animalType(self):
        print(f'The animal type is: {self.animalType}')


class Pets(Animals):
    def __init__(self, petType):
        self.petType = petType

    def petType(self):
        print(f'The pet type is: {self.petType}')

class Dog(Pets):
    @staticmethod
    def bark():
        print('Bow bow!')


d = Dog(petType='dog')
d.bark()

