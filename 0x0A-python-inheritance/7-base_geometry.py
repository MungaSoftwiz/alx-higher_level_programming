#!/usr/bin/python3
""" Module named 7-base_geometry """


class BaseGeometry:
    """ A class that raises an Exception"""

    def area(self):
        """ A public instance method that raises an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A public instance method that validates value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= zero
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
