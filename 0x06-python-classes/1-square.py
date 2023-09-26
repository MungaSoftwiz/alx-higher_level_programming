#!/usr/bin/python3
"""A module with a class definition, Square"""


class Square:
    """A class definition of the class, Square

    An __init__ method to initialise the instance
    attributes

    Args:
        size (int): The size of the square

    Attributes:
        __size (int): A private instance attribute

    """

    def __init__(self, size):
        self.__size = size
