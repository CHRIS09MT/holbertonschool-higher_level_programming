#!/usr/bin/python3
"""Module that defines an empty class Rectangle."""


class Rectangle:
    """Represents an empty rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""

        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
