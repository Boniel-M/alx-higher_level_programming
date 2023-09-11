#!/usr/bin/python3
"""
This module defines the MyList class that inherits from the list class.
"""


class MyList(list):
    """
    A custom list class that provides additional functionality.

    Public methods:
    - print_sorted(self): Print the list in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending order."""
        print(sorted(self))
