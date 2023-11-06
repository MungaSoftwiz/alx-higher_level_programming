#!/usr/bin/python3
""" Module has one function is_same_class() """


def is_same_class(obj, a_class):
    """ Function checks if object is exactly an
    instance of the specified class
    """
    return type(obj) is a_class
