import math
import numbers
from abc import ABC, abstractmethod
"""
abc : module name (build in module)
ABC: Abstract class in abc module
abstractmethod : annotations that can be given to abstract methods
if you need all the modules of abc you may import like import abc, than class Shape(abc.ABC) and 
method annotation should be @abc.abstractmethod
"""
class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass
class Shape(ABC):
    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square (Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side

class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return math.pow(self.radius) * math.pi


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> numbers:
        return self.width * self.length


class Cube(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):

    def area(self) -> numbers:
        pass

    def volume(self):
        pass

square = Square(8)

print(square.area())
print(square)
