#!/usr/bin/python3
"""Create a class"""


class BaseGeometry:
    """
    Implemented the Exception error
    Check if the value is an int and if is less or equal than 0
    """
    def area(self):
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be gerater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    subclass Rectanlge
    create two private instantation
    and validated with integer_validator
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
