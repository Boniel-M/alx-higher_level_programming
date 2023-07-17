#!/usr/bin/python3

"""
This module contains the base class for all other classes in the project.
"""


class Base:
    """
    Base class for managing the id attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): Optional id for the instance.

        Attributes:
            id (int): Public instance attribute representing the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
