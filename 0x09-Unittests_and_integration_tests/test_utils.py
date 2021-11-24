#!/usr/bin/env python3
""" Tests for utils.py """
import json
import requests
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ This class will test the function
        access_nested_map in utils.py
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Test for correct functioning """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test for fail conditions """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Test the function get_json in utils.py"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, test_payload):
        """ Use mock to test an http call and json return """
        with patch('requests.get') as mock_request:
            mock_request().json.return_value = test_payload
            mock_request.assert_called_once()
            result = get_json(url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class for memoize test"""

    def test_memoize(self):
        """
        Test that when calling a_property twice,
        the correct result is returned but a_method
        is only called once using assert_called_once
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            first = test.a_property
            second = test.a_property
            self.assertEqual(first, 42)
            self.assertEqual(second, 42)
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
