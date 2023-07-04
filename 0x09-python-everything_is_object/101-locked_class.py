#!/usr/bin/python3

"""
This module contains the LockedClass which prevents the user from dynamically
creating new instance attributes, except for the `first_name` attribute.
"""


class LockedClass:
    """
    LockedClass enforces restrictions on dynamically creating
    new instance attributes.
    """
    __slots__ = ["first_name"]
