"""
Importing JSON
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    serialize and save to file
    """

    with open(filename, "w", encoding="utf-8") as file:
        serialize = json.dumps(data)
        file.write(serialize)


def load_and_deserialize(filename):
    """
    load and deserialize
    """

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
