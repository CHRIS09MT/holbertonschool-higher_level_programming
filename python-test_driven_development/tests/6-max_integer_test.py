#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer function"""
    
    def test_max_at_end(self):
        """Test where the maximum value is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-10, -20, -30, 0]), 0)
        self.assertEqual(max_integer([100, 200, 300, 400, 500]), 500)

    def test_max_at_beginning(self):
        """Test where the maximum value is at the beginning of the list"""
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
        self.assertEqual(max_integer([0, -10, -20, -30]), 0)
        self.assertEqual(max_integer([500, 100, 200, 300, 400]), 500)

    def test_max_in_middle(self):
        """Test where the maximum value is in the middle of the list"""
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)
        self.assertEqual(max_integer([-10, -20, 0, -30]), 0)
        self.assertEqual(max_integer([100, 200, 500, 300, 400]), 500)

    def test_one_negative_number(self):
        """Test with a list containing only one negative number"""
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([-1]), -1)

    def test_only_negative_numbers(self):
        """Test with a list of only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -5]), -5)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

if __name__ == '__main__':
    unittest.main()
