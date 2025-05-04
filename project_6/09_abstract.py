# Use the abc module to create an abstract class Shape with an abstract method area(). 
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract method that must be overhidden in subclasses

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # Implementing the abstract method

rect = Rectangle(5, 10)  # Creating an object of Rectangle class
print(f"Area of Rectangle: {rect.area()}")  