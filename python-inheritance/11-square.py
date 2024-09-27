#!/usr/bin/python3
"""Square module"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Calculate and return the area of the square"""

        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """return the area of the square"""

        return self.__size * self.__size
