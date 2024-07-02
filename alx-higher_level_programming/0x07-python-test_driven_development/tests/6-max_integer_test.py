#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_simple_strings(self):
        maxint = max_integer("This string")
        self.assertEqual(maxint, 't')
    
    def test_simple_strings(self):
        maxint = max_integer((12563, 0, 8.45, "rew"))
        self.assertEqual(maxint, 9)

    def test_simple_strings(self):
        maxint = max_integer([1, 6, 100])
        self.assertEqual(maxint, 100)

    def test_list_of_strings(self):
        maxint = max_integer(["Holberton", "School", "98"])
        self.assertEqual(maxint, "School")

    def test_list_of_floats(self):
        maxint = max_integer([1.5, 8.8, 3.9])
        self.assertEqual(maxint, 8.8)

    def test_mixed_types(self):
        self.assertRaises(TypeError, max_integer,[3.142, 98, "Holberton"])

    def test_empty_list(self):
        maxint = max_integer([])
        self.assertEqual(maxint, None)

    def test_empty_string(self):
        maxint = max_integer("")
        self.assertEqual(maxint, None)

    def test_homo_tuple_values(self):
        maxint = max_integer((1.5, 8.8, 3.9))
        self.assertEqual(maxint, 8.8)

    def test_het_tuple_values(self):
        self.assertRaises(TypeError, max_integer,(3.142, 98, "Holberton"))

    def test_dict_values(self):
        self.assertRaises(KeyError, max_integer, {"pi":3.142,"num":98,"str":"Holberton"})

    def test_None(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_list_of_length_one(self):
        maxint = max_integer([98])
        self.assertEqual(maxint, 98)

    def test_list_of_complex_numbers(self):
        self.assertRaises(TypeError, max_integer, [2j, 9j, 8, 89j])

    def test_list_and_mixed(self):
        self.assertRaises(TypeError, max_integer, [3.142, [1, 2, 0], 98, "Dark"])


if __name__ == "__main__":
    unittest.main()
