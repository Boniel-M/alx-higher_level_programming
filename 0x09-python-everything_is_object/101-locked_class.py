#!/usr/bin/python3


"""
This module contains the LockedClass which prevents the user from dynamically
creating new instance attributes, except for the `first_name` attribute.
"""


class LockedClass:
    """LockedClass enforces restrictions on dynamically creating new instance
    attributes."""

    def __setattr__(self, attr, value):
        """Set the value of the specified attribute.

        Args:
            attr (str): The name of the attribute to set.
            value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute being set is not `first_name`.
        """
        if attr != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'"
                                 .format(attr))
        self.__dict__[attr] = value
