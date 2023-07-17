#!/usr/bin/python3

"""
Unit tests for the Base module.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test case for the Base class.
    """

    def test_id_assignment(self):
        """
        Test the assignment of IDs in the Base class.

        - Create multiple instances of Base.
        - Verify that the ID values are assigned correctly.
        """

        obj1 = Base()
        obj2 = Base()
        obj3 = Base(100)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 100)


if __name__ == '__main__':
    unittest.main()
