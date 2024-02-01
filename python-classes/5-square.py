#!/usr/bin/python3
"""
    Create a class call Square
"""


class Square:
    """
        Define a square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            Return a the current aquare area
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an interger")
        if value <0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size is 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.__size * "#")
