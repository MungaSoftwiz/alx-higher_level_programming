#!/usr/bin/python3
""" Module contains function inherits_from() """


def inherits_from(obj, a_class):
    """ Function checks if object is an instance of a class,
    that inherited (directly or indirectly) from specified class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
