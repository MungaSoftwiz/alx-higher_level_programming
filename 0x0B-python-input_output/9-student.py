#!/usr/bin/python3
""" Module defines a class """


class Student:
    """
    A class Student

    Attributes:
        first_name (str): First name of student instance
        last_name (str): Last name of Student instance
        age (int): The age of the Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
