#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
from urllib import request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    # make a request to the url
    req = request.Request(url)

    # open the response as res and read it 
    with request.urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
