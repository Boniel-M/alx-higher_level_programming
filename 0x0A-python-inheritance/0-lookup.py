#!/usr/bin/python3

"""
a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Returns a sorted list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list object containing the sorted names of attributes and methods.

    """
    return sorted(dir(obj))
