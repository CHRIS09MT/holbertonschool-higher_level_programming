#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer function"""
    
    def test_normal_case(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([5]), 5)
    
    def test_negative_numbers(self):
        """Test with a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -3]), -3)
    
    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
    
    def test_mixed_numbers(self):
        """Test with a list of mixed positive and negative integers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([0, -1, -2, 3]), 3)

if __name__ == '__main__':
    unittest.main()
