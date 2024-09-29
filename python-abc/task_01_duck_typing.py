from abc import ABC, abstractmethod
import math


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
        self.__radius = radius

    """
    Implement the 'area' method to calculate the area of the circle
    """

    def area(self):
        return math.pi * (self.__radius**2)

    """
    Implement the 'perimeter' method to calculate the perimeter of the circle
    """

    def perimeter(self):
        return 2 * math.pi * self.__radius

    """
    'Rectangle' class that inherits from 'Shape'
    """


class Rectangle(Shape):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    """
    Implement the 'area' method to calculate the area of ​​the rectangle
    """

    def area(self):
        return self.__width * self.__height

    """
    Implement the 'perimeter' method to calculate the perimeter
    of the rectangle
    """

    def perimeter(self):
        return 2 * (self.__height + self.__width)


"""
'shape_info' function that accepts any object with the
'area' and 'perimeter' methods
"""


def shape_info(object):
    print(f"Area: {object.area()}")
    print(f"Perimeter: {object.perimeter()}")
