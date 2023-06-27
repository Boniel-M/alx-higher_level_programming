#!/usr/bin/python3

import math
"""
    A class that represents a magic circle with radius.
"""


class MagicClass:
    """
    A class that represents a magic circle with radius.

    Attributes:
        __radius (float or int): The radius of the magic circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance.

        Args:
            radius (float or int): The radius of the magic circle.
                Defaults to 0.

        Raises:
            TypeError: If the radius is not a number (float or int).
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
