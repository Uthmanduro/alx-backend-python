#!/usr/bin/env python3
"""parameterize a unit test"""
import requests
import unittest
from unittest.mock import Mock, patch
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


class TestGetJson(unittest.TestCase):
    """implement the test suite for utils.get_json"""
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """Test get_json function."""
        with patch('requests.get', return_value=Mock(
                json=lambda: test_payload)) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """implement the test suite for utils.memoize"""
    def test_memoize(self):
        """Test memoize function."""
        class TestClass:
            """TestClass for memoize function."""
            def a_method(self):
                """a_method for memoize function."""
                return 42

            @memoize
            def a_property(self):
                """a_property for memoize function."""
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42)\
                as mock_method:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)
            mock_method.assert_called_once()
