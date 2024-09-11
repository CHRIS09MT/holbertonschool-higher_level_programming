#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = {clave: valor * 2 for clave, valor in a_dictionary.items()}

    return b_dictionary
