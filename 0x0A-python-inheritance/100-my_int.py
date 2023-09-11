#!/usr/bin/python3
"""
This module defines the MyInt class.
"""


class MyInt(int):
    """
    A rebel class inheriting from int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Override the equality (==) operator to invert its behavior.

        Args:
            other: The value to compare against.

        Returns:
            bool: True if the values are not equal; False if they are equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality (!=) operator to invert its behavior.

        Args:
            other: The value to compare against.

        Returns:
            bool: True if the values are equal; False if they are not equal.
        """
        return super().__eq__(other)


if __name__ == "__main__":
    a = MyInt(4)
    b = MyInt(4)
    c = MyInt(5)

    print(a == b)  # Should print False (inverted == operator)
    print(a != b)  # Should print True (inverted != operator)

    print(a == c)  # Should print True (inverted == operator)
    print(a != c)  # Should print False (inverted != operator)
