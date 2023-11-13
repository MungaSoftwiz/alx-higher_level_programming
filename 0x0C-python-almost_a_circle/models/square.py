#!/usr/bin/python3
""" Module has a Square class that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class defines a Square; a subclass of Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Gets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Arguments:
            value (int): the size value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Method updates the arguments of the attributes

        Arguments:
            args: A list of positional arguments
            kwargs: A list of key, value pairs
        """
        attr = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                setattr(self, attr[idx], arg)
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Method returns the dictionary representation of a
        Square
        """
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict

    def __str__(self):
        """
        Method returns the readable str representation of an instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
