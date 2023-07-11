#!/usr/bin/python3

"""
The function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation (string).

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
