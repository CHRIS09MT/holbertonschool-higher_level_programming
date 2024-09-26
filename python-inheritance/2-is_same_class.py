#!/usr/bin/python3
"""
The function checks if an object is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class"""

    return type(obj) is a_class
