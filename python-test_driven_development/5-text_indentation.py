#!/usr/bin/python3

"""
Adds two new lines after each '.', '?', and ':' in the text.
Ensures the input is a valid string and handles formatting.
"""


def text_indentation(text):
    """
    Prints text with two new lines after '.', '?', and ':'.
    Raises TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"

            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1

    formatted_result = "\n".join(line.strip() for line in result.split("\n"))

    print(formatted_result, end="")
