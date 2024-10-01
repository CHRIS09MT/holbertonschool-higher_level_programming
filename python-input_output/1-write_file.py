#!/usr/bin/python3
"""
write and count the amount the characters of a file
"""


def write_file(filename="", text=""):
    """
    write in file
    """

    with open(filename, "w", encoding="utf-8") as file:
        count = file.write(text)
    return count
