#!/usr/bin/python3
def roman_to_int(roman_string):
    num_roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

    if not isinstance(roman_string, str):
        return 0

    result = 0
    lenght = len(roman_string)

    for i in range(lenght):
        current_value = num_roman[roman_string[i]]

        if i + 1 < lenght and current_value < num_roman[roman_string[i + 1]]:
            result -= current_value
        else:
            result += current_value

    return result
