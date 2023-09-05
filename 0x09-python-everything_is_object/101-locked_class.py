#!/usr/bin/python3


"""
This module defines the LockedClass, which
attributes except for 'first_name'.
"""


class LockedClass:
    def __setattr__(self, name, value):
        """
        Custom __setattr__ method to restrict attribute assignment.
        Raises AttributeError if the attribute is not 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        super().__setattr__(name, value)

    def __delattr__(self, name):
        """
        Custom __delattr__ method to restrict attribute deletion.
        Raises AttributeError if the attribute is not 'first_name'.
        """
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        super().__delattr__(name)
