#!/usr/bin/python3

def no_c(my_string):
    cut_string = ""

    for char in my_string:
        if char != "c" and char != "C":
            cut_string += char
    return cut_string
