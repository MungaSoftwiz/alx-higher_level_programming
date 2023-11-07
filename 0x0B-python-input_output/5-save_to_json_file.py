#!/usr/bin/python3
""" Module contains function save_to_json_file """

import json


def save_to_json_file(my_obj, filename):
    """ Function writes an object to a text file using
    JSON string representation
    """

    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
