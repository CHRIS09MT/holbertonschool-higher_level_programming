#!/usr/bin/python3
"""
This module defines a function `print_square` to print a square of hash
(`#`) characters based on the given size.
"""


def print_square(size):
    """
    Prints a square of hash (`#`) characters.

    Args:
        size (int): The size of the square. Must be a non-negative integer.
    """

    if size is None:
        raise ValueError("size cannot be None")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
