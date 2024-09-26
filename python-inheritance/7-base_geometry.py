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
        """"""

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
