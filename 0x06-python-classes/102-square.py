#!/usr/bin/python3
class Square:
    """
    This class represents a square.

    Attributes:
        size (float or int): The size of the square.

    Methods:
        area(): Calculate the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If the size is not a number.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare two Square instances for equality based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare two Square instances for inequality based on their areas.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the areas are not equal,
            False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Compare two Square instances to check if the area of
        the first square is greater than the second square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of the first square
            is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Compare two Square instances to check if the area of
        the first square is greater than or equal to the second square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of the first square
            is greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Compare two Square instances to check if the area of the first square
        is less than the second square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of the first square is less,
            False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Compare two Square instances to check if the area of the first square
        is less than or equal to the second square.

        Args:
            other (Square): The other Square instance to compare.

        Returns:
            bool: True if the area of the first square
            is less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
