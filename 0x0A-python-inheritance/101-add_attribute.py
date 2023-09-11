#!/usr/bin/python3
"""
This module defines the add_attribute function.
"""


def add_attribute(obj, attr, value):
    """
    Add a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)


if __name__ == "__main__":
    class Example:
        def __init__(self, initial_value):
            self.initial_value = initial_value

    obj = Example(42)
    add_attribute(obj, "new_attr", "new_value")
    print(obj.new_attr)
