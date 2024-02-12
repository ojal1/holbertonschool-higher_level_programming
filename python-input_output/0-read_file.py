#!/usr/bin/python3
"""Module: 0-read_file"""


def read_file(filename=""):
    """Function that reads a text file"""

    with open(filename, "r", encoding="utf-8") as my_file:
        content = my_file.read()
        print("{}".format(content), end="")
