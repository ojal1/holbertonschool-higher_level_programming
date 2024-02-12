#!/usr/bin/python3
"""Create a class call Base"""


class Base:
    """define the base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
