#!/usr/bin/python3

"""
Defines a function that prints a formatted name.
Validates that both inputs are strings.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>' after validation.
    Raises TypeError if first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
