#!/usr/bin/python3
"""Module for converting a JSON string to an object."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
