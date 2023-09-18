#!/usr/bin/python3

"""Square Module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle and represents a square with a
    side length, position (x, y), and an ID.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The side length of the square.
            x (int, optional): The x-coordinate of the square's position
                (default is 0).
            y (int, optional): The y-coordinate of the square's position
                (default is 0).
            id (int, optional): The ID of the square (default is None).

        Raises:
            TypeError: If any of the arguments (size, x, or y) is not an int.
            ValueError: If size is not greater than 0, or if x or y is < 0.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The side length of the square (read-only property).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Square instance with provided argument
        in the following order:
        1st argument: id attribute
        2nd argument: size attribute
        3rd argument: x attribute
        4th argument: y attribute

        Args:
            *args: The values to update the attributes with.
            **kwargs: The key-value pairs to update the attributes with.
        """
        if args:
            arg_names = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
