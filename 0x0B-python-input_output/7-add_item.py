#!/usr/bin/python3
""" Module contains script to add args to a python list """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    python_object = load_from_json_file("add_item.json")
except FileNotFoundError:
    python_object = []

python_object.extend(sys.argv[1:])
save_to_json_file(python_object, "add_item.json")
