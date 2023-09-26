#!/usr/bin/python3
"""A module that defines a class named square"""


class Square:
    """A class that defines a square with validations

    Attributes:
        __size (int): The private instance attribute
    """

    def __init__(self, size=0):
        """The __init__ method initialises instances attribute

        Args:
            size (int): The size of the square

        Raises:
            TypeError: Raised if size is not an integer
            ValueError: Raised if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
