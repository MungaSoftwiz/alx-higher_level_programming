#!/usr/bin/python3
""" Module contains an  empty class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A child class inherits from BaseGeometry """

    def __init__(self, width, height):
        """ Instantiate the rectangle class """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """ Method to return the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Return the string representation """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
