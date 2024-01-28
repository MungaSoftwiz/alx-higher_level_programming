#!/usr/bin/python3
""" The 1-hbtn_header.py module"""

import sys
import urllib.request


if __name__ == "__main__":
    """
    Sends a request to the URL and displays value of the
    X-Request-Id variable found in header of the response
    """
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
