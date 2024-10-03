#!/usr/bin/python3
"""
Function to write an Object to a text file using JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize the object
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
