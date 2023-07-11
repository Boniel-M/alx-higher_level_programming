#!/usr/bin/python3

"""
a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
