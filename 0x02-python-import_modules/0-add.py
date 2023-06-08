#!/usr/bin/python3

"""program that imports the function def add(a, b): from the file add_0.py"""

import add_0 as add

a = 1
b = 2

sum = add.add(a, b)

print("{} + {} = {}".format(a, b, sum))
print("", end="")
