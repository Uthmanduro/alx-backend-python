#!/usr/bin/env python3
"""A github org client that parameterizes and patch as decorators"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """implements the testorg method"""
    @parameterized.expand([("google"), ("abc")])
    def test_org(self, org_name):
        """tests the org method"""
        with patch('client.get_json') as mock_get:
            test_class = GithubOrgClient(org_name)
            test_class.org()
            mock_get.assert_called_once_with(test_class.ORG_URL.format
                                             (org=org_name))
