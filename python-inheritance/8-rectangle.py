#!/usr/bin/python3
"""Module of geometry"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """
        messenger of exception
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
