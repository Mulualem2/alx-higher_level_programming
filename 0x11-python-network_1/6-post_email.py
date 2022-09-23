#!/usr/bin/python3
'''
That takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally
displays the body of the response.
'''

import requests
import sys

if __name__ == '__main__':
    email_value = {'email': sys.argv[2]}
    email_r = requests.post(sys.argv[1], data=email_value)
    print("{}".format(email_r.text))
