#!/usr/bin/python3

"""
a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
