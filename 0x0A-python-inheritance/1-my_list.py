#!/usr/bin/python3
""" Module has a class MyList """


class MyList(list):
    """ The MyList class """

    def print_sorted(self):
        """ Function prints a list in sorted order """
        sorted_list = sorted(self)
        print(sorted_list)
