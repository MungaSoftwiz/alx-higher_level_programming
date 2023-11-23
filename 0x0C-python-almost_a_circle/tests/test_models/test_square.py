import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """ TestSquare class inherits from unittest
    for testing the square class
    """

    def test_init_with_valid_args(self):
        """ Test case with valid arguments """
        square = Square(5, 4, 3, 12)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 12)

    def test_init_two_arguments(self):
        """ Test for two arguments to Square"""
        square = Square(1, 2)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)

    def test_init_three_arguments(self):
        """ Test for three arguments to Square """
        square = Square(1, 2, 3)
        self.assertEqual(square.width, 1)
        self.assertEqual(square.height, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_init_strings(self):
        """ Test with init strings with two  arguments """
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_init_strings(self):
        """ Test with string with three  arguments"""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_init_with_invalid_arguments(self):
        """ Test case with invalid arguments"""
        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(TypeError):
            Square()

        with self.assertRaises(ValueError):
            Square(-5)

        with self.assertRaises(TypeError):
            Square(5.5)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_str(self):
        """ Test square string method """
        s1 = Square(5, 4, 3, 12)
        expected = "[Square] (12) 4/3 - 5"
        self.assertEqual(str(s1), expected)

    def test_update_method(self):
        """ Test the square update method"""
        s2 = Square(5)

        s2.update(10)
        self.assertEqual(s2.id, 10)

        s2.update(1, 2)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)

        s2.update(1, 2, 3, 4)
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.width, 2)
        self.assertEqual(s2.height, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)

        s2.update(size=7, y=1, id=89)
        self.assertEqual(s2.width, 7)
        self.assertEqual(s2.y, 1)
        self.assertEqual(s2.id, 89)


class TestSquareCreate(unittest.TestCase):
    """ Test the create method """
    def test_create_with_id(self):
        """ Test create with id """
        square = Square.create(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_create_with_width(self):
        """ Test with width """
        sqr = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(sqr.width, 1)
        self.assertEqual(sqr.id, 89)

    def test_create_with_x(self):
        """ Test with x value """
        s = Square.create(**{
            'id': 89,
            'size': 1,
            'x': 2
        })
        self.assertEqual(s.id, 89)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(r.x, 2)

    def test_create_with_x(self):
        """ Test with y value """
        s = Square.create(**{
            'id': 89,
            'size': 1,
            'x': 3,
            'y': 4,
        })
        self.assertEqual(s.id, 89)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
