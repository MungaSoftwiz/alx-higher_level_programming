#!/usr/bin/python3
""" Module defines a Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class inherits from rectangle """
    def __init__(self, size):
        """ Call the parent class constructor with __init__ """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ Return the area of the square """
        return self.__size ** 2
