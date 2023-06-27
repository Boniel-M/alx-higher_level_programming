#!/usr/bin/python3
"""
This module defines a class Square that represents a square shape.

"""


class Square:
    """ A class representing a square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
