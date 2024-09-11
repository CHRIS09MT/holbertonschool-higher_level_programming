#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    return [[num ** 2 for num in row] for row in matrix]
