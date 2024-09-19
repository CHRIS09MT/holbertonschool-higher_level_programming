#!/usr/bin/python3
"""Module that defines an empty class Square."""


class Square:
    """Represents an empty square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with a private size attribute."""

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for the position attribute."""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position attribute. Validates the value."""

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Returns the area of the square."""

        return self.__size * self.__size

    def my_print(self):
        """"""

        if self.__size <= 0:
            print()
            return

        for j in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
