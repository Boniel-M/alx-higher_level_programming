#!/usr/bin/python3

def lookup(obj):
    """
    Returns a sorted list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list object containing the sorted names of attributes and methods.

    """
    return sorted(dir(obj))
