#!/usr/bin/python3
"""Module: 1-write_file"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file
    and return the numbers of characters
    """

    with open(filename, 'w', encoding="utf-8") as my_file:
        my_file.write(text)
        return len(text)