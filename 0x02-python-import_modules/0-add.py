#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

"""program that imports the function def add(a, b): from the file add_0.py"""
from add_0 import add as Boniel
    a = 1
    b = 2

    sum = Boniel(a, b)

    print("{} + {} = {}".format(a, b, sum))
    print("", end="")
