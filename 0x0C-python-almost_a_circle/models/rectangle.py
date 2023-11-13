#!/usr/bin/python3
""" Module defines class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """ Class defines a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Property gets width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Arguments:
            value (int): the width value

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Sets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Arguments:
            value (int): the width value

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets the x coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter sets the width of the rectangle

        Arguments:
            value (int): the width value

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter sets the width of the rectangle

        Arguments:
            value (int): the width value

        Raises:
            TypeError: If `value` is not an integer
            ValueError: If `value` is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method computes the area of the rectangle

        Returns: The area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Method prints to the stdout the rectangle using `#`
        """
        print(self.__y * "\n", end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Methos updates the arguments of the attributes

        Arguments:
            args: A list of positional arguments
            kwargs: A list of key, value pairs
        """
        attr = ["id", "width", "height", "x", "y"]
        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                setattr(self, attr[idx], arg)

        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method returns the dictionary representation of a
        Rectangle
        """
        rectangle_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rectangle_dict

    def __str__(self):
        """
        Method returns the readable representation of an instance
        """
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))
