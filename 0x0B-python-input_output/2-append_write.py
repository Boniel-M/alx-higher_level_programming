#!/usr/bin/python3

"""
a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Write a string to a text file and return the number of characters written

    Args:
        filename (str): The name of the text file.
        Defaults to an empty string.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.

    Example:
        characters_written = write_file("example.txt", "Hello, World!")
        print(characters_written)  # Output: 13
    """
    with open(filename, "a", encoding="utf-8") as file:
        characters_added = file.write(text)

    return characters_added
