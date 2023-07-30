#!/usr/bin/env python3
"""parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected_Result):
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected_Result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map function."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)