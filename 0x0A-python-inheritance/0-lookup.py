#!/usr/bin/python3

"""
Look up module
"""


def lookup(obj):
    """
    Get a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the attributes and objects.
    """
    return dir(obj)
