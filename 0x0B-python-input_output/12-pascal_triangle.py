#!/usr/bin/python3

"""
The Module create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
        n (int): The number of rows in the Pascal's Triangle.

    Returns:
        list: A list of lists representing Pascal's Triangle.
    """
    triangle = []

    if n <= 0:
        return triangle

    for row in range(n):
        current_row = [1] * (row + 1)

        for i in range(1, row):
            current_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]

        triangle.append(current_row)

    return triangle
