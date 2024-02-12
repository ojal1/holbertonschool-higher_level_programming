#!/usr/bin/python3
"""Module: 3-to_json_string"""


import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object"""

    return json.dumps((my_obj))
