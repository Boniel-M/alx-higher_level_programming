#!/usr/bin/python3


"""
This module contains the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle's position (default: 0).
            y (int): Y coordinate of the rectangle's position (default: 0).
            id (int): Optional id for the instance.

        Attributes:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X coordinate of the rectangle's position.
            y (int): Y coordinate of the rectangle's position.
            id (int): Public instance attribute representing the id.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width to be set.

        Raises:
            ValueError: If the width is not a positive integer.
            TypeError: If the width is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")
        if value <= 0:
            raise ValueError("width must be > 0.")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height to be set.

        Raises:
            ValueError: If the height is not a positive integer.
            TypeError: If the height is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")
        if value <= 0:
            raise ValueError("height must be > 0.")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The x coordinate to be set.

        Raises:
            ValueError: If the x coordinate is not an integer or is < than 0.
            TypeError: If the x coordinate is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0.")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The y coordinate to be set.

        Raises:
            ValueError: If the y coordinate is not an integer or is < than 0.
            TypeError: If the y coordinate is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0.")
        self.__y = value

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle by printing it to stdout.

        The rectangle is represented by '#' characters.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the rectangle with the provided arguments.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
                Key: Attribute name.
                Value: Attribute value.
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i >= len(attributes):
                    break
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
