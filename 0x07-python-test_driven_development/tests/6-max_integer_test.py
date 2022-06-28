#!/usr/bin/python3
"""Test file for max_integer([..]) exercise
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestingMaxInteger(unittest.TestCase):
    def test_max(self):
        """Test the max integer on integers"""
        self.assertEqual(max_integer(list=[7, 10, 22, 36]), 3)
        self.assertEqual(max_integer(list=[2, 39, 1, 10]), 3)
        self.assertEqual(max_integer(list=[-1000, 0, -42, -150]), 0)
        self.assertEqual(max_integer(list=[-100, -110, -400, -150]), -100)

    def test_empty(self):
        """Test if the list is empty"""
        self.assertIsNone(max_integer(list=[None]))
        self.assertIsNone(max_integer(list=[]))

    def test_errors(self):
        """Test possible errors in the code"""
        self.assertRaises(TypeError, max_integer, list=[2, "Hello", 3])
        self.assertRaises(TypeError, max_integer, list=[[1, 2, 3], 100, 100.6])
        self.assertRaises(TypeError, max_integer, list=[(1, 2), 100, 100.6])

if __name__ == '__main__':
    unittest.main()
