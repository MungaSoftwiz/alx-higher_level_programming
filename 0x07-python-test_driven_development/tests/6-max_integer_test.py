#!/usr/bin/python3
""" A test module for testing a function that finds maximum value in a list """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """  Class tests cases for the max_integer function """

    def test_max_beginning(self):
        """ tests for maximum value at beginning of the list """
        beginning = [7, 6, 4, 1]
        self.assertEqual(max_integer(beginning), 7)

    def test_max_end(self):
        """ tests for maximum value at the end of a list """
        end = [1, 4, 6, 7]
        self.assertEqual(max_integer(end), 7)

    def test_max_middle(self):
        """ tests for maximum value at the middle of a list """
        middle = [1, 4, 7, 6, 3]
        self.assertEqual(max_integer(middle), 7)

    def test_two_max(self):
        """ tests for occurencee of two maximum values """
        two_max = [1, 4, 7, 6, 7]
        self.assertEqual(max_integer(two_max), 7)

    def test_empt_list(self):
        """ tests for an empty list """
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """ tests for maximum value in a one element list """
        single_element_list = [7]
        self.assertEqual(max_integer(single_element_list), 7)

    def test_negative_values(self):
        """ tests for maximum values in a list with negative values """
        with self.subTest():
            """ tests for one negative value """
            self.assertEqual(max_integer([1, 4, -7, 6, 3]), 6)
        with self.subTest():
            """ tests for a list with all negative values """
            self.assertEqual(max_integer([-1, -4, -7, -6, -3]), -1)

    def test_ints_and_floats(self):
        """ tests for maximum value in a list with ints and floats """
        mixed_list = [7, 3, 5.5,18.11, 18]
        self.assertEqual(max_integer(mixed_list), 18.11)

    def test_ints_and_floats(self):
        """ tests for maximum vlvalue in a list of strings """
        string = ["Software", "engineering", "is", "fun"]
        self.assertEqual(max_integer(string), "is")

if __name__ == '__main__':
    unittest.main()
