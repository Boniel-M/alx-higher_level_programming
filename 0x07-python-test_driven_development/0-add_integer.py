#!/usr/bin/python3

"""This module defines an integer addition function add_integer(a, b=98).
    Module-level docstring line 2.
    Module-level docstring line 3.
    Module-level docstring line 4.
    Module-level docstring line 5."""


def add_integer(a, b=98):
    """
    Adds two integers. Function-level docstring line 2, 3, and 4.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
