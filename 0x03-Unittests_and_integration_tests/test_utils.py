#!/usr/bin/env python3
"""
module to test access_nested_map function
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock
from utils import get_json


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
