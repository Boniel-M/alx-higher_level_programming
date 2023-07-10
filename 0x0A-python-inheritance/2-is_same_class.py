#!/usr/bin/python3
"""
Check if obj is instance of a_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class;
        otherwise False.

    """
    return obj.__class__ is a_class
