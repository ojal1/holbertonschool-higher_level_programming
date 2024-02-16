#!/usr/bin/python3
"""Create a class call Base"""


import json


class Base:
    """define the base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        if list_objs is None:
            list_objs = []
        # create the file name of class in .json
        filename = f"{cls.__name__}.json"
        # save the list of objects to a file
        list = []
        for obj in list_objs:
            list.append(obj.to_dictionary())
        # search of the file name with .json
        with open(filename, "w") as f:
            json_str = cls.to_json_string(list)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return json_string"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)
