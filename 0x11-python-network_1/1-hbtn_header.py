#!/usr/bin/python3
""" takes a URL, sends a request and returns"""


import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        print("{}".format(response.getheader('X-Request-Id')))
