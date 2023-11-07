#!/usr/bin/python3
""" Module contains load_from_json_file function """

import json


def load_from_json_file(filename):
    """ Function cretaes an object from a JSON file """

    with open(filename) as f:
        return json.load(f)
