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

a = 1
b = 2

sum = add(a, b)

print("{} + {} = {}".format(a, b, sum))
print("", end="")
