#!/usr/bin/python3

"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inherits from Base and represents a rectangle with width,
    height, position (x, y), and an ID.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position
            (default is 0).
            y (int, optional): The y-coordinate of the rectangle's position
            id (int, optional): The ID of the rectangle (default is None).

        Raises:
            TypeError: If any of the arguments (width, height, x, or y)
            is not an integer.
            ValueError: If width or height is not greater than 0,
            or if x or y is less than 0
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        int: The width of the rectangle (read-only property).
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        int: The height of the rectangle (read-only property).
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        int: The x-coordinate of the rectangle's position (read-only property)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x-coordinate attribute.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        int: The y-coordinate of the rectangle's position (read-only property)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y-coordinate attribute.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
