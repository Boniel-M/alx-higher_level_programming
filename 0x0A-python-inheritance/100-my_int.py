#!/usr/bin/python3

"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
    Class representing a rebellious integer.
    Inherits from int.
    """

    def __eq__(self, other):
        """
        Equality operator.

        Args:
            other (int): The value to compare against.

        Returns:
            bool: True if the values are not equal, False otherwise.

        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inequality operator.

        Args:
            other (int): The value to compare against.

        Returns:
            bool: True if the values are equal, False otherwise.

        """
        return super().__eq__(other)
