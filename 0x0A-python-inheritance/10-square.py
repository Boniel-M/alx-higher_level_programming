#!/usr/bin/python3
"""
Module: 10-square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class that represents a square.
    Inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not a positive integer.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.

        """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
