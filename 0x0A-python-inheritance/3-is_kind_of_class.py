#!/usr/bin/python3
""" Module has one function is_kind_of_class() """


def is_kind_of_class(obj, a_class):
    """ Function checks if object is an instance of,
    or if object is an instance of a class that inherited
    from specified class
    """
    return isinstance(obj, a_class)
