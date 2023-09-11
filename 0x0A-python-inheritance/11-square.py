#!/usr/bin/python3
"""
This module defines the Square class.
"""


class BaseGeometry:
    """
    A class for geometric operations.
    """

    def area(self):
        """
        Compute the area (not implemented).

        Raises:
            Exception: Always raises an Exception with the message
            "area() is not implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the input value as an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class for representing rectangles.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>".
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class for representing squares.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>".
        """
        return "[Square] {}/{}".format(self.__size, self.__size)


if __name__ == "__main__":
    s = Square(4)

    print(s)
    print("Area:", s.area())
