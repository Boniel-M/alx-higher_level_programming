#!/usr/bin/python3
"""Base Module"""

import json  # Import the json module


import json

class Base:
    """
    Base class represents the base of all other classes in the project.
    It manages the 'id' attribute in all future classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
