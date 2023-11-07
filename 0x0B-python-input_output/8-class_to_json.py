#!/usr/bin/python3
""" Module contains function class_to_json """


def class_to_json(obj):
    """ Function returns the dictionary description with simple
    data structures for JSON serialization of an object
    """

    return obj.__dict__
