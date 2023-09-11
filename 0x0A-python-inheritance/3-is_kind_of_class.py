#!/usr/bin/python3
"""
This module defines a function to check if an object is
an instance of a specified class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of,
    or if it is an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if the object is an instance of,
        or its subclass is an instance of,
        the specified class; otherwise, False.
    """
    return isinstance(obj, a_class)
