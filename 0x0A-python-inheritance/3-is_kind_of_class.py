#!/usr/bin/python3
"""
A Function is_kind_of_class that Check class inheritance
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of or inherited from a_class

    Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise, returns False.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class; otherwise, False.

    """
    return isinstance(obj, a_class)
