#!/usr/bin/python3
"""Module: 2-append_write"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file"""

    with open(filename, 'a', encoding='utf-8') as my_file:
        my_file.write(text)
        return len(text)
