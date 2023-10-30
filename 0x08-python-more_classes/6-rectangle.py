#!/usr/bin/python3
""" The module defines `Rectangle` class """


class Rectangle:
    """
    An implementation of a `Rectangle` class

    Attributes:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        A method to return the string representation of an object

        Return:
            str: The readable string representation of an instance
        """

        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for _ in range(self.__height):
            result += '#' * self.__width + '\n'
        return result.rstrip()

    def __repr__(self):
        """
        A method to return the string representation of an object

        Return:
            str: The official string representation of an instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    @property
    def width(self):
        """
        A property to get the value of the width

        Return:
            int: The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        A setter method to set the width of the rectangle

        Arguments:
            value (int): The value set as the width

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        A property to get the value of the height

        Return:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A setter method to set the height of the rectangle

        Arguments:
            value (int): The value set as the height

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than zero
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        An instance method to the equate the rectangle's area

        Return:
            int: The area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        An instance method to the equate the rectangle's perimeter

        Return:
            int: The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
