#!/usr/bin/python3
"""
a class MyList that inherits from list
"""

class MyList(list):
    """
    Custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).

        """
        sorted_list = sorted(self)
        print(sorted_list)
