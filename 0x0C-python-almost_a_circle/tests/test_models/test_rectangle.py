#!/usr/bin/python3
"""unitest for testing rectangle"""

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingRectangle(unittest.TestCase):
    """class for Test Rectangle"""

    # RECTANGLE WIDTH CHECKER
    def test0_width_few_args(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r0 = Rectangle(1)

    def test1_width_string(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r1 = Rectangle("hello", 2)

    def test2_width_list(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r2 = Rectangle([9, 6], 2)

    def test3_width_tuple(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r3 = Rectangle((7, 3), 4)

    def test4_width_dictionary(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r4 = Rectangle({'k': 8}, 5)

    def test5_width_zero(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(ValueError):
                r5 = Rectangle(0, 6)

    def test6_width_negative(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(ValueError):
                r6 = Rectangle(-7, 8)

    def test7_width_float(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r7 = Rectangle(4.5, 9)

    def test8_width_nan(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r8 = Rectangle(float('NaN'), 7)

    def test9_width_inf(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r9 = Rectangle(float('inf'), 7)
