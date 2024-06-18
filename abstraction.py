from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width 

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Creating instance of circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(6, 4)

# Accesing area and perimeter
print(f"Circle: Area = {circle.area()}, Perimeter = {rectangle.perimeter()}") 
print(f"Rectangle: Area = {rectangle.area()}, Perimeter = {rectangle.perimeter()}") 
