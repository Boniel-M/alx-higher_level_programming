#!/usr/bin/python3
"""
This module provides a function to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the text file to read.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
