#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sqrd_mtrx = [[element ** 2 for element in row] for row in matrix]
    return sqrd_mtrx
