#!/usr/bin/python3
"""Module for creating an object from a JSON file
and writing an object to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
