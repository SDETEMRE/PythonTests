from typing import final

PI: final = 3.14
@final
class Animal:
    pass

class Dog(Animal):
    pass

class Employee:
    @final
    def work(self):
        print('Working')
class Driver(Employee):
    def work(self):
        print('Driving')