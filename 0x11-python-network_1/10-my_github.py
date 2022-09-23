#!/usr/bin/python3
'''
Takes your Github credentials (username and password) and uses
the Github API to display your id
'''

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(argv[1], argv[2]))
    if response.status_code == 200:
        dictionary = response.json()
        print(dictionary['id'])
    else:
        print(None)
