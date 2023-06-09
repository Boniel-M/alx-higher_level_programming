#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for nums in row:
            print("{}".format(nums), end="")
        print()
