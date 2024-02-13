#!/usr/bin/python3
"""Create a class call Rectangle"""


from models.base import Base


class Rectangle(Base):
    """define the Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.validator("width", width)
        self.validator("height", height)
        self.validator("x", x)
        self.validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def validator(self, name_att, value):
        """Create a method to validate the input"""

        if type(value) is not int:
            raise TypeError(f"{name_att} must be an integer")
        if name_att == "width" or name_att == "height":
            if value <= 0:
                raise ValueError(f"{name_att} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{name_att} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        self.validator("width", value)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.validator("height", value)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        self.validator("x", value)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        self.validator("y", value)
