#!/usr/bin/python3
""" Module contains the to_json_string function """

import json


def to_json_string(my_obj):
    """ Function returns the JSON representation of an object(string """

    json_string = json.dumps(my_obj)
    return json_string
