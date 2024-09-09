#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
    	print(" ".join("{:2}".format(i) for i in row))
