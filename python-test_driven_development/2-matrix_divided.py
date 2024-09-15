#!/usr/bin/python3

"""
Module: matrix_divided

This module contains a function `matrix_divided` that performs element-wise -
division on a matrix.
The matrix is a list of lists containing integers or floats.
The function ensures the matrix is properly formatted and the divisor is -
valid before performing the division.

Function:
matrix_divided(matrix, div)

Arguments:
matrix: A matrix represented as a -
list of lists.
Each element in the matrix must be an integer or a float.
All rows in the matrix must have the same number of columns.
div (int/float): The divisor used to divide each element of the matrix.
It must be either an integer or a float and cannot be zero.

Returns:
list of lists of float: A new matrix where each element has been divided -
by `div` and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A matrix where each element is an integer or float.
    """

    if not isinstance(matrix, list):
        raise TypeError(
            """matrix must be a matrix (list of lists)
                        of integers/floats"""
        )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            """matrix must be a matrix (list of lists)
                        of integers/floats"""
        )

    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])

    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix
