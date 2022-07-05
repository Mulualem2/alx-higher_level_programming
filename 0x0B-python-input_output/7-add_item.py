#!/usr/bin/python3
"""add an item"""
from sys import argv
import json
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

for arg in range(1, len(argv)):
    my_list.append(argv[arg])
save_to_json_file(my_list, "add_item.json")
