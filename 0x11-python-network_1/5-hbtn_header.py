#!/usr/bin/python3
""" The 5-hbtn_header.py module """

import sys
import requests


if __name__ == "__main__":
    """ Displays X-Request-Id header variable value """
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
