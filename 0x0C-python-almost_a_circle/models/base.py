#!/usr/bin/python3
""" A base module base.py to keep track of instances IDs """

import json


class Base:
    """
    Class manages the id attribute of all future classes

    Attriutes:
        __nb_objects: Private class attribute
        id (int): The id attribute of the instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method that serializes dictionaries to json string

        Arguments:
            list_dictionaries (list): The list of dictionaries

        Returns: A json string representation of the object
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method saves the json string of list_objs  to a file

        Arguments:
            cls: The class
            list_objs (list): The list objects to be saved
        """
        if list_objs is None:
            list_objs = []
        file_name = cls.__name__ + ".json"
        j_str = cls.to_json_string([lst.to_dictionary() for lst in list_objs])
        with open(file_name, mode="w", encoding="UTF8") as f:
            f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Method desirializes a json string

        Arguments:
            json_string: The string representation of the list

        Returns: The list of the JSON string representation
        """
        if json_string is None and len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Method creates an instance with all attributes

        Arguments:
            cls: The class
            dictionary: A douple pointer to a dictionary

        Returns: An instance with all attributes
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(7, 11)
        else:
            dummy = cls(7)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Method loads a string from a file

        Arguments:
            cls: The class
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, encoding="UTF8") as f:
                json_string = f.read()
                dcts = cls.from_json_string(json_string)

                instances = [cls.create(**dct) for dct in dcts]
                return instances
        except FileNotFoundError:
            return []
