#!/usr/bin/python3
"""
Read a file useding utf-8
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to standard output.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content, end="")
