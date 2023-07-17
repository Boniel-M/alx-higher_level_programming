#!/usr/bin/python3


"""
This module contains unit tests for the Rectangle class.
"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        """
        Test the constructor of the Rectangle class.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        """
        Test the area method of the Rectangle class.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        """
        Test the display method of the Rectangle class.
        """
        r = Rectangle(3, 3)
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        """
        Test the __str__ method of the Rectangle class.
        """
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/3 - 5/10")

    def test_update_args(self):
        """
        Test the update method of the Rectangle class with positional argument
        """
        r = Rectangle(5, 10)
        r.update(7, 3, 4, 1, 2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        """
        Test the update method of the Rectangle class with keyword arguments.
        """
        r = Rectangle(5, 10)
        r.update(id=7, width=3, height=4, x=1, y=2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)


if __name__ == '__main__':
    unittest.main()
