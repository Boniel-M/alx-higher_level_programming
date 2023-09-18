#!/usr/bin/python3
"""
Base Module
"""

import json


class Base:
    """
    Base class for managing id attributes in derived classes.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance.

        Args:
            id (int, optional): The ID of the instance (default is None).
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances to be saved to a file.

        Raises:
            TypeError: If list_objs is not a list of instances derived Base.
        """
        if list_objs is None:
            list_objs = []

        if not isinstance(list_objs, list):
            raise TypeError("list_objs must be a list of instances")

        instance_list = [obj.to_dictionary() for obj in list_objs]
        filename = cls.__name__ + ".json"

        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(instance_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Parse a JSON string and return a list of dictionaries.

        Args:
            json_string (str): The JSON string to be parsed.

        Returns:
            list: A list of dictionaries represented by json_string.
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create and return an instance with attributes set based on dictionary

        Args:
            **dictionary (dict): A dictionary containing attribute values.

        Returns:
            Base: An instance with attributes set as per the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a "dummy" Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a "dummy" Square instance

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Load and return a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_str = file.read()
                obj_dicts = cls.from_json_string(json_str)
                return [cls.create(**d) for d in obj_dicts]
        except FileNotFoundError:
            return []
