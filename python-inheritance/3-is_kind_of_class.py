#!/usr/bin/python3
"""
This module defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance or inherited instance of a_class.
    """

    return isinstance(obj, a_class)
