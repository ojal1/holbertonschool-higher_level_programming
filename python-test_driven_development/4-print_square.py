#!/usr/bin/python3
"""Module: 4-print_square.py"""


def print_square(size):
    """size - size of square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)
