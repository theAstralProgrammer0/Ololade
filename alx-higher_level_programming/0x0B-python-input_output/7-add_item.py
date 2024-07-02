#!/usr/bin/python3
"""This is a script that adds all arguments to a Python list, and then save
   them to a file:
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file = "add_item.json"
args = sys.argv[1:]

try:
    with open(json_file, mode="r") as myFile:
        myFile.read()
except FileNotFoundError:
    save_to_json_file(args, json_file)
else:
    save_to_json_file(load_from_json_file(json_file) + args, json_file)
