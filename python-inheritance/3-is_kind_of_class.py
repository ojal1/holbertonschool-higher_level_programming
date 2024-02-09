#!/usr/bin/python3
"""
Function that returns True if
the object is an instance, otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Return True or Flase"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
