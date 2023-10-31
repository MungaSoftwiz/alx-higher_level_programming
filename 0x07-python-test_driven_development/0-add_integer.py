#!/usr/bin/python3
""" A module that adds of two numbers """


def add_integer(a, b=98):
    """
    Function add two numbers and returns the result

    Arguments:
        a (int, float): The first argument
        b (int, float): The constant second argument

    Raises:
        TypeError: Raised if one of the arguments is not an integer

    Return: The addition of the two arguments
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result
