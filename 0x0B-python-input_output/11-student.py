#!/usr/bin/python3

"""
a class Student that defines a student
"""


class Student:
    """
    a class Student that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve.
            Defaults to None

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance based
        on the provided JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None
        """
        for attr, value in json.items():
            setattr(self, attr, value)
