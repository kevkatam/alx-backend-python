#!/usr/bin/python3
"""
module to test access_nested_map function
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any


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
