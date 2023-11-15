#!/usr/bin/python3
""" Test module for base.py """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Tests the base class """

    def test_base(self):
        """ Tests the correct id without id """
        b = Base()
        self.assertTrue(b.id, 0)

    def test_init_with_id(self):
        """ Tests init with an id """
        b1 = Base(id=12)
        self.assertEqual(b1.id, 12)

    def test_init_without_id(self):
        """ Tests for init without an id """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, b2.id - 1)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b3.id, b4.id - 1)

    def test_id_uniqueness(self):
        """ Test uniqueness of the id """
        b1 = Base()
        b2 = Base()
        self.assertNotEqual(b1.id, b2.id)

    def nan_id(self):
        """ Test not a number """
        self.assertEqual(float('nan'), Base(float('nan')).id)


class TestBaseToJsonString(unittest.TestCase):
    """ Tests of the to_json_string method """

    def test_to_json_string_with_none(self):
        """ Tests if none is passed """
        result = Base.to_json_string(None)
        self.assertEqual(result, [])

    def test_to_json_string_with_empty_str(self):
        """ Tests if passed an empty value it will exist """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_list_of_dict(self):
        """ Tests if dict is passed returns a string"""
        data = [{"id": 12}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_if_it_returns_str(self):
        """ Tests if the method returns a string """
        data = [{"id": 12}]
        result = Base.to_json_string(data)
        self.assertEqual(type(result), type('str'))


class TestBaseFromJsontring(unittest.TestCase):
    """ Tests of the from_json_string method """

    def test_from_json_string_with_none(self):
        """ Testing if None is passed """
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_with_empty_str(self):
        """ Tests return if an empty string is passed"""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_with_a_string(self):
        """ Tests return value if string is passed"""
        json_string = '[{"id": 89}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 89}])

    def test_from_json_string_if_it_returns_list(self):
        """ Tests if method returns a list """
        json_string = '[{"id": 89}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(type(result), type([]))
