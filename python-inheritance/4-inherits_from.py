#!/usr/bin/python3
"""
This module defines the is_kind_of_class function.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance or inherited /
    (directly or indirectly) instance of a_class
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
