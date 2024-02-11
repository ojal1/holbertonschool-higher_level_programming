#!/usr/bin/python3
"""Create a class call Square that inherits from Rectanglea"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)