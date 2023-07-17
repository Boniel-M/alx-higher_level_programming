#!/usr/bin/python3

"""Manage object ID assignment."""


class Base:
    """
    Base class to manage id attribute for all classes in the project.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base object.

        Args:
            id (int, optional): ID value to assign to the object.
            Defaults to None.

        Notes:
            - If `id` is provided, assign it to the
            public instance attribute `id`.
            - If `id` is not provided, increment the
            private class attribute `__nb_objects`
              and assign its new value to the public instance attribute `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
