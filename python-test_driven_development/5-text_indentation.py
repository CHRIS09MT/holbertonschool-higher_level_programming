#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    next_text = ""
    
    for char in text:
        next_text += char
        if char in '.?:':
            next_text += "\n\n"
        print(next_text.strip())