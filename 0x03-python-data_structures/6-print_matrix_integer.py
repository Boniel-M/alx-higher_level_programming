#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            """# Print the number with a space separator"""
            print("{:d}".format(num), end=" ")

            """# Print a newline character after the last number in the row"""
            if i == len(row) - 1:
                print()

    """# Print an empty line if the matrix is empty"""
    if not matrix:
        print()
