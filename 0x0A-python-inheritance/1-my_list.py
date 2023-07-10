#!/usr/bin/python3

"""
a class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Public Methods:
        print_sorted: Prints the list in ascending order.

    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """

        sorted_list = sorted(self)
        print(sorted_list)
