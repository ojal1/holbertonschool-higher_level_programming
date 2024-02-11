#!/usr/bin/python3
"""My list inherits from list"""


class Mylist(list):
    """Print inheritance from list"""

    def print_sorted(self):
        print(sorted(self))
