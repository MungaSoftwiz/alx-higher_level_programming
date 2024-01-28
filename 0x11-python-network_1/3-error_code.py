#!/usr/bin/python3
""" The 3-error_code.py module"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    """ Send request to an URL and view response body """
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
