#!/usr/bin/python3
""" Module contains function from_json_string """

import json


def from_json_string(my_str):
    """ Function returns object representation of a JSON string """

    loaded_data = json.loads(my_str)
    return loaded_data
