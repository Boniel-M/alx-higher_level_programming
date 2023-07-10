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

        Example:
            >>> my_list = MyList()
            >>> my_list.append(1)
            >>> my_list.append(4)
            >>> my_list.append(2)
            >>> my_list.append(3)
            >>> my_list.append(5)
            >>> my_list.print_sorted()
            [1, 2, 3, 4, 5]

        """
        sorted_list = sorted(self)
        print(sorted_list)
