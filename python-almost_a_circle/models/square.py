#!/usr/bin/python3
"""Class call Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(self, size, size, x, y, id)

    def __str__(self):
        """string representation"""
        my_string = "[Square] ({}) ".format(self.id)
        my_string += "{}/{} ".format(self.x, self.y)
        my_string += "- {}".format(self.width)
        return my_string