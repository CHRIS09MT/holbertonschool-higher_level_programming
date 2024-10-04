#!/usr/bin/python3
"""
creating a Student class
"""


class Student:
    """
    defining a class of a student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns the dictionary description with simple data structure
        """

        return self.__dict__
