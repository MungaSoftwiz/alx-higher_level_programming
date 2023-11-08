#!/usr/bin/python3
""" Module of 11-square.py """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    def __init__(self, size):
        """ Initialization private attribute size and validation"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ Method that calculates area of a square """
        return self.__size ** 2

    def __str__(self):
        """ Method prints and returns the readable representation of object """
        return str("[Square] {}/{}".format(self.__size, self.__size))
