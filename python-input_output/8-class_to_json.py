#!/usr/bin/python3
"""
returns the dictionary description
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """

    return obj.__dict__
