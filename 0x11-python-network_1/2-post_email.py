#!/usr/bin/python3
""" The 2-post_email.py module """

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    """ Sends a POST request to a given URL with an email """
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email).encode("ascii")

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
