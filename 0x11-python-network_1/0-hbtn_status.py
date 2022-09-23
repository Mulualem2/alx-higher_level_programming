#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request

url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as response:
    the_page = response.read()
    print('Body response:')
    print('\t- type: {}'.format(type(the_page)))
    print('\t- content: {}'.format(the_page))
    print('\t- utf8 content: {}'.format(the_page.decode('utf-8')))
