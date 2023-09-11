#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    A class for geometric operations.
    """

    def area(self):
        """
        Compute the area (not implemented).

        Raises:
            Exception: Always raises an Exception with the message
            "area() is not implemented."
        """
        raise Exception("area() is not implemented")
