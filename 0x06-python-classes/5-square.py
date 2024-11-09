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
        """
        self.__size = size

    @property
    def size(self):
        """Method gets size of the square

        Returns:
            the size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square to value

        Args:
            value (int): the value to be set

        Raises:
            TypeError: Raised if size is not an integer
            ValueError: Raised if size is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Method finds the square area

        Returns:
            the square area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """Method prints a square to the standard output
        """

        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end="")
            print()
