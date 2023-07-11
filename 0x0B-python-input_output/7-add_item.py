#!/usr/bin/python3
"""
a script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
from os.path import exists
from typing import List
from json import dump, load


def save_to_json_file(my_obj: List, filename: str) -> None:
    """Save object to a JSON file."""
    with open(filename, 'w') as file:
        dump(my_obj, file)


def load_from_json_file(filename: str) -> List:
    """Load object from a JSON file."""
    if not exists(filename):
        return []
    with open(filename, 'r') as file:
        return load(file)


if __name__ == '__main__':
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, filename)
