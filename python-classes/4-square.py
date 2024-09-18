#!/usr/bin/python3
"""Module that defines an empty class Square."""


class Square:
    """Represents an empty square."""

    def __init__(self, size=0):
        """Initializes the square with a private size attribute."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute."""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute. Validates the value."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Returns the area of the square."""

        return self.__size * self.__size
