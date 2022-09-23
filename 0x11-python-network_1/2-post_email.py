#!/usr/bin/python3
"""Python script that post an email"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email_value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(email_value)
    data = data.encode('utf-8')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print("{}".format(response.read().decode('utf-8')))
