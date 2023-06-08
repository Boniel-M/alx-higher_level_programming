#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    addition = add(a, b)
    substrac = sub(a, b)
    multiply = mul(a, b)
    division = div(a, b)

    print("{} + {} = {}".format(a, b, addition))
    print("{} - {} = {}".format(a, b, substrac))
    print("{} * {} = {}".format(a, b, multiply))
    print("{} / {} = {}".format(a, b, division))
