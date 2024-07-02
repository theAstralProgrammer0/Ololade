#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
from urlliib import request


if __name__ == "__main__":
    url = sys.argv[1]

    # make a request
    req = request.Request(url)

    # open response as res
        print(dict(res.headers).get("X-Request-Id"))
    with request.urlopen(req) as res:
