#!/usr/bin/python3
"""A module that defines a class named square"""


class Square:
    """A class that defines a square with private instance attributes
    """
    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method initialises instances attribute

        Attributes:
            __size (int): Private instance attribute
            __position (tuple): Private instance attribute
        """
        self.__size = size
        self.__position = position

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
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Method sets the position of spaces

        Returns:
            the position of spaces
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of square with preceding spaces

        Args:
            value (int): the value to be set

        Raises:
            TypeError: Raised if position is not a tuple
            of 2 positive integers
        """
        if (not isinstance(value, tuple or
            len(value) != 2 or
                all(isinstance(num, int) and num >= 0 for num in value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method finds the square area

        Returns:
            the square area
        """
        return self.__size ** 2

    def my_print(self):
        """Method prints a square to the standard output
        with positions preceded by spaces
        """
        if self.__size == 0:
            print()
        # Print the vertical space
        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
