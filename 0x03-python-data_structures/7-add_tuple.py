#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """# Extract the first two elements from tuple_a, or
    use 0 if the tuple is smaller than 2"""

    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    """ # Extract the first two elements from tuple_b,
    #or use 0 if the tuple is smaller than 2"""
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    """# Perform addition of corresponding elements
    and return the resulting tuple"""
    return a1 + b1, a2 + b2
