#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a[:2] if len(tuple_a) >= 2 else (0, 0)
    b1, b2 = tuple_b[:2] if len(tuple_b) >= 2 else (0, 0)

    sum_1 = a1 + b1
    sum_2 = a2 + b2

    return sum_1, sum_2
