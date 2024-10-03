#!/usr/bin/python3
"""
Module that contains a function to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end and returns the number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
