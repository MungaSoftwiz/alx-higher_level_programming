#!/usr/bin/python3
""" The 4-hbtn_status.py module"""

import requests


if __name__ == "__main__":
    """ Fetches https://alx-intranet.hbtn.io/status with requests library """
    req = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
