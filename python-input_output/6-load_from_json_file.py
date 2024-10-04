#!/usr/bin/python3
"""
creating a object
"""

import json


def load_from_json_file(filename):
    """
    creating a object
    """

    with open(filename, "r") as file:
        return json.load(file)
