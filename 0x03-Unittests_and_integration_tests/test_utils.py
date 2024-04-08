#!/usr/bin/env python3
"""
module to test access_nested_map function
"""
from utils import access_nested_map, get_json, memoize
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """ class to test access_nested_map function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, n: Mapping, p: Sequence, r: Any) -> None:
        """ test case for access_nested_map"""
        result = access_nested_map(n, p)
        self.assertEqual(result, r)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
            self,
            n: Mapping,
            p: Sequence,
            r: Any
            ) -> None:
        """ test case for key error raised """
        with self.assertRaises(r):
            access_nested_map(n, p)


class TestGetJson(unittest.TestCase):
    """ class used to test get_json """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, url: str, r: bool, mock_get: Dict) -> None:
        """ method that tests get_json function """
        mock_response = Mock()
        mock_response.json.return_value = r

        with patch('requests.get', return_value=mock_response):
            result = get_json(url)
            self.assertEqual(result, r)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ testcase for memoize class """

    def test_memoize(self):
        """ method to test the memoize method """
        class TestClass:
            """ testclass containing example function """
            def a_method(self):
                """ method example to be decorized by memoize """
                return 42

            @memoize
            def a_property(self):
                """ memoized decorated method """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test_obj = TestClass()
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            mock.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
