#!/usr/bin/python3

def fizzbuzz():
    output = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            output.append("FizzBuzz")
        elif i % 3 == 0:
            output.append("Fizz")
        elif i % 5 == 0:
            output.append("Buzz")
        else:
            output.append(str(i))
    print(' '.join(output), end=' ')
