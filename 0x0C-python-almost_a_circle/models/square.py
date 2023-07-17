#!/usr/bin/python3


"""
This module contains the Square class.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square (same for width and height).
            x (int): X coordinate of the square's position (default: 0).
            y (int): Y coordinate of the square's position (default: 0).
            id (int): Optional id for the instance.

        Attributes:
            size (int): Size of the square (same for width and height).
            x (int): X coordinate of the square's position.
            y (int): Y coordinate of the square's position.
            id (int): Public instance attribute representing the id.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The size to be set.

        Raises:
            ValueError: If the size is not a positive integer.
            TypeError: If the size is not an integer.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square with the provided arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
                Key: Attribute name.
                Value: Attribute value.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attributes):
                    break
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the square.

        Returns:
            dict: The dictionary representation of the square.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
