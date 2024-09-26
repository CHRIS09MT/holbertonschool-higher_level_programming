#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """Inherits from list and has a method to print a sorted the list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""

        print(sorted(self))

    def is_same_class(obj, a_class):
        """Returns True if obj is exactly an instance of a_class"""

        return type(obj) == a_class
