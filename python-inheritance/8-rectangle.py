#!/usr/bin/python3
"""Create a class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """
    subclass Rectanlge
    create two private instantation
    and validated with integer_validator
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("heigth", height)
        self.__width = width
        self.__height = height 
