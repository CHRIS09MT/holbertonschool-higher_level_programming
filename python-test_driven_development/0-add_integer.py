#!/usr/bin/python3
"""
This module contains a function `add_integer` that adds two integers.
The function takes two arguments and returns their sum after converting
any float arguments to integers.
"""


def add_integer(a, b=98):
    """Sum two integers.
    Args: a: first integer argument. | b: second integer argument.
    return the sum of the two integers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a or b != b:
        raise ValueError("cannot convert float NaN to integer")

    if abs(a) == float("inf"):
        raise OverflowError("cannot convert float infinity to integer")

    a = int(a)
    b = int(b)

    return a + b
