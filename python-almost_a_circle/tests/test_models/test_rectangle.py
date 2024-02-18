#!/usr/bin/python3
"""Unittest for Rectangle class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class
        Rectangle __init__(width,height,x=0,y=0,id=none)
    """

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0

    def test_rectangle_creation(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_string(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_five_arguments(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_rectangle_negative_numbers(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)

    def test_rectangle_zero_values(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0)

    def test_area_method_exists(self):
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_str_method_exist(self):
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 3/4 - 1/2')

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

if __name__ == "__main__":
    unittest.main()