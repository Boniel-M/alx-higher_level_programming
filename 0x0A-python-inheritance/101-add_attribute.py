#!/usr/bin/python3

"""
a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attribute: The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object does not support adding new attributes.

    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
