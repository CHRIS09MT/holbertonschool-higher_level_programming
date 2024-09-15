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

    i = 0
    result = ""
    
    while i < len(text):
        if text[i] in ".?:":  # Si encuentra un signo de puntuación
            result += text[i] + "\n\n"  # Agrega el signo y dos saltos de línea
            i += 1
            while i < len(text) and text[i] == " ":  # Saltar espacios adicionales
                i += 1
            continue
        result += text[i]
        i += 1

    print(result.rstrip())  # Elimina cualquier espacio o salto extra al final
