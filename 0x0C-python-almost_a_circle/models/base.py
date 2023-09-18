#!/usr/bin/python3

"""Base class module"""


class Base:
    """Base class with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """If an id is provided, assign it to the
            public instance attribute 'id' """
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
