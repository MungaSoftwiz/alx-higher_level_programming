#!/usr/bin/python3
""" Module contains tests for rectangle.py """

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Includes methods to test the id of instances """
    def test_rectangle_id(self):
        rect = Rectangle(10, 2, 0, 0, 1)
        self.assertEqual(rect.id, 1)

        rect = Rectangle(2, 10, 0, 0, 2)
        self.assertEqual(rect.id, 2)

        rect = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(rect.id, 12)

    def test_instantiation(self):
        """ Tests attribute validation """
        rect = Rectangle(10, 5, 2, 3)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_init_with_zero(self):
        """ Tests for zero width or height """
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_negative_attributes(self):
        """ Test instantiation witt invalid values """
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)

        with self.assertRaises(ValueError):
            Rectangle(10, -5)

        with self.assertRaises(ValueError):
            Rectangle(10, 5, -2)

        with self.assertRaises(ValueError):
            Rectangle(10, 5, 2, -3)

    def test_non_integers(self):
        """ Test for non-integers """
        with self.assertRaises(TypeError):
            Rectangle("ten", 5)

        with self.assertRaises(TypeError):
            Rectangle(10, ("Five",))

        with self.assertRaises(TypeError):
            Rectangle(10, 5, float('inf'), 3)

        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, ['t', 'h', 'r', 'e', 'e'])


class TestRectangleArea(unittest.TestCase):
    """ Test case for testing of the area method """

    def test_area(self):
        """ Tests for the area method """
        rect = Rectangle(3, 2)
        self.assertEqual(rect.area(), 6)

        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

        rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rect.area(), 56)

    def test_area_negative(self):
        """ Tests for area with negative value """
        with self.assertRaises(ValueError):
            Rectangle(-3, 2).area()

        with self.assertRaises(ValueError):
            Rectangle(2, -10).area()

        with self.assertRaises(ValueError):
            Rectangle(-8, -7, 0, 0, 12).area()

    def test_area_non_integer(self):
        """ Tests for area with string value """
        with self.assertRaises(TypeError):
            Rectangle("three", 2).area()

        with self.assertRaises(TypeError):
            Rectangle(3, (2,)).area()

        with self.assertRaises(TypeError):
            Rectangle(8, [7], 0, 0, 12).area()
