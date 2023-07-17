#!/usr/bin/python3

"""
Module with Base class
"""


import json
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string representation to a list of dictionaries.

        Args:
            json_string (str): JSON string representation.

        Returns:
            list: List of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes set from a dictionary.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: An instance of the class with attributes set from the
            dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a file.

        Returns:
            list: List of instances.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [
                        cls.create(**dictionary) for dictionary in dictionaries
                        ]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes a list of instances to a CSV file.

        Args:
            list_objs (list): List of instances.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is None or len(list_objs) == 0:
                writer.writerow([])
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer.writerow(fieldnames)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size,
                                         obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from a CSV file.

        Returns:
            list: List of instances.
        """
        file_name = cls.__name__ + ".csv"
        instances = []
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]),
                                       int(row[3]), int(row[0]))
                    instances.append(instance)
        except FileNotFoundError:
            pass
        return instances
