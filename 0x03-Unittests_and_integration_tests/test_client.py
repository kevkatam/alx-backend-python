#!/usr/bin/env python3
"""
module for TestGithubOrgClient
"""
from client import GithubOrgClient
import unittest
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ testcase class for GithubOrgClient"""
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True}),
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str , r: Dict, mock_get_json: Dict) -> None:
        """ method to test org function """
        mock_get_json.return_value = r
        github_client = GithubOrgClient(org_name)

        org_info = github_client.org
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

        self.assertEqual(org_info, r)
