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

    def test_set_x_y_non_integer(self):
        """ Test non int values for setter methods x & y """
        rect = Rectangle(10, 5)
        with self.assertRaises(TypeError):
            rect.x = 6.2
            rect.y = 7.9

    def test_set_x_y_negative_values(self):
        """ Test negative values for setter methods x & y """
        rect = Rectangle(10, 5)
        with self.assertRaises(ValueError):
            rect.x = -6
            rect.x = -7


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

    def test_str(self):
        """ Test for the __str__ method """
        rect = Rectangle(6, 4, 3, 7, 12)
        expected = "[Rectangle] (12) 3/7 - 6/4"
        self.assertEqual(str(rect), expected)

class TestRectangleUpdate(unittest.TestCase):
    """ Tests the update method in Rectangle """
    def test_update_with_valid_args(self):
        rect = Rectangle(10, 5)

        rect.update(77, 8, 7, 6, 2)
        self.assertEqual(rect.id, 77)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 7)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 2)

    def test_update_with_no_x_and_y(self):
        rect = Rectangle(10, 5)
        rect.update(23, 12)

        self.assertEqual(rect.id, 23)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_update_with_no_args(self):
        """ Test for an empty value call to update method """
        rect = Rectangle(10, 5, 0, 0, 6)
        rect.update()

        self.assertEqual(rect.id, 6)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_update_with_kwargs(self):
        """ Test for instance when kwargs are passed to update """
        rect = Rectangle(10, 10, 10, 10)
        rect.update(y=6, width=5, x=10, id=34)

        self.assertEqual(rect.id, 34)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 6)

    def test_to_dictionary(self):
        """ Test to dictionary function """
        rect = Rectangle(3, 2, 3, 2, 7)
        expected = {'id': 7, 'width': 3, 'height': 2, 'x': 3, 'y': 2}
        self.assertEqual(rect.to_dictionary(), expected)

class TestRectangleCreate(unittest.TestCase):
    """Testing the create method """
    def test_create_with_id(self):
        """ Test create with id """
        rect = Rectangle.create(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_create_with_width(self):
        """Test with width """
        rect = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.id, 89)

    def test_create_with_height(self):
        """ Test with height """
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_create_with_x(self):
        """ Test with x coordinate"""
        rect = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3
        })
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_create_with_y(self):
        """ Test with y coordinate"""
        rect = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
        })
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
