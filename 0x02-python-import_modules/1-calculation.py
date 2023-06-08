#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    addition = add(a, b)
    print("{} + {} = {}".format(a, b, addition))

    substrac = sub(a, b)
    print("{} - {} = {}".format(a, b, substrac))

    multiply = mul(a, b)
    print("{} * {} = {}".format(a, b, multiply))

    division = div(a, b)
    print("{} / {} = {}".format(a, b, multiply))
