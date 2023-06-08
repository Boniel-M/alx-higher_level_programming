#!/usr/bin/python3

if __name__ == "__main__":
    from add_0 import add

"""program that imports the function def add(a, b): from the file add_0.py"""

a = 1
b = 2

sum = add(a, b)

print("{} + {} = {}".format(a, b, sum))
print("", end="")
