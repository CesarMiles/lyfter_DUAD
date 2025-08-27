from abc import ABC, abstractmethod
import math 

#Abstract class to designate methods to be used be  other shapes 
class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass 
    
    @abstractmethod
    def calculate_area(self):
        pass 

#Other shapes will be defined downbelow 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter
    
    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        self.perimeter = 4 * self.side
        return self.perimeter
    
    def calculate_area(self):
        self.area = self.side ** 2
        return self.area


class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    
    def calculate_perimeter(self):
        self.perimeter = 2 * (self.lenght + self.width)
        return self.perimeter

    def calculate_area(self):
        self.area = self.lenght * self.width
        return self.area
    

#Testing area 

square = Square(4)
circle = Circle(4)
rectangle = Rectangle(6, 3)

print(rectangle.calculate_perimeter())