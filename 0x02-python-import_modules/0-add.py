#!/usr/bin/python3

"""program that imports the function def add(a, b): from the file add_0.py"""

from add_0 import add

a = 1
b = 2

sum = add(a, b)

print("{} + {} = {}".format(a, b, sum))
print("", end="")

if __name__ == "__main__":
    add(a, b)
