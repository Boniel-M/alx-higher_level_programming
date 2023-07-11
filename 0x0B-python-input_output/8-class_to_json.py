#!/usr/bin/python3


"""
a function that returns the dictionary description with simple data structure
"""


def class_to_json(obj):
    """
    Return a dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: A dictionary description of the object with
        serializable attributes
    """
    attributes = obj.__dict__
    serialized = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[key] = value
    return serialized
