#!/usr/bin/python3
"""Class call Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation"""
        my_string = "[Square] ({}) ".format(self.id)
        my_string += "{}/{} ".format(self.x, self.y)
        my_string += "- {}".format(self.width)
        return my_string

    def update(self, *args, **kwargs):
        """Assing attributes to each argument"""
        my_list = ['id', 'size', 'x', 'y']
        if args:
            for name, value in zip(my_list, args):
                setattr(self, name, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value
