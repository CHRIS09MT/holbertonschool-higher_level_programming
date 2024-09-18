#!/usr/bin/python3
"""Module that defines an empty class Square."""


class Square:
    """Represents an empty square."""

    def __init__(self, size=0):
        """Initializes the square with a private size attribute."""

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
