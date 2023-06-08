#!/usr/bin/python3

def magic_calculation(a, b):

    """function emulates the behavior of the given Python bytecode"""
    add, sub = __import__("magic_calculation_102", fromlist=("add", "sub"))

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
