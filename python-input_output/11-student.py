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

    def to_json(self, attrs=None):
        """
        returns the dictionary description with simple data structure
        """

        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            filtered_dict = {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
            return filtered_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        iterate over the 'json' dictionary
        """

        for key, value in json.items():
            setattr(self, key, value)
