from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract class 'Shape' that defines the abstract methods
    'area' and 'perimeter'
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    """
    'Circle' class that inherits from 'Shape'
    """


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    """
    Implement the 'area' method to calculate the area of the circle
    """

    def area(self):
        return abs(3.141592653589793 * self.__radius**2)

    """
    Implement the 'perimeter' method to calculate the perimeter of the circle
    """

    def perimeter(self):
        return abs(2 * 3.141592653589793 * self.__radius)

    """
    'Rectangle' class that inherits from 'Shape'
    """


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    """
    Implement the 'area' method to calculate the area of ​​the rectangle
    """

    def area(self):
        return self.width * self.height

    """
    Implement the 'perimeter' method to calculate the perimeter
    of the rectangle
    """

    def perimeter(self):
        return 2 * (self.height + self.width)


"""
'shape_info' function that accepts any object with the
'area' and 'perimeter' methods
"""


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
