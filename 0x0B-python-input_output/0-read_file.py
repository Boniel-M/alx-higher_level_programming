#!/usr/bin/python3

"""
The function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Read the contents of a text file and print them to stdout.

    Args:
        filename (str): The name of the text file to read

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Notes:
        - The text file must be encoded in UTF-8.
        - This function uses the 'with' statement to ensure proper file
          handling.
        - No extra newline is added between lines when printing to stdout.

    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
