#!/usr/bin/python3

"""
a function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written

    Args:
        filename (str): The name of the text file. Defaults to an empty string
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        num_characters = file.tell()

    return num_characters
