#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """Inherits from list and has a method to print a sorted version of the list"""

    def print_sorted(self):
        """Prints the list sorted in ascending order"""

        print(sorted(self))
