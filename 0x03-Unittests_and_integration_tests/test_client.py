#!/usr/bin/env python3
"""A github org client that parameterizes and patch as decorators"""


import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from typing import Callable


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

    def test_public_repos_url(self):
        """tests the _public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "twitter.com"}
            result = mock_org.return_value
            test_class = GithubOrgClient("twitter")
            self.assertEqual(test_class._public_repos_url, result["repos_url"])

    @patch('client.get_json', return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, p_get_json: Callable):
        """Tests client.GithubOrgClient.public_repos"""
        resp = {'repos_url': 'https://api.github.com/orgs/Google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, return_value=resp)\
                as m_org:
            org = GithubOrgClient('Google')
            # self.assertEqual(org._public_repos_url, resp['repos_url'])
            self.assertEqual(org.public_repos(),
                             ['episodes.dart', 'cpp-netlib',
                              'dagger', 'ios-webkit-debug-proxy',
                              'google.github.io', 'kratu',
                              'build-debian-cloud', 'traceur-compiler',
                              'firmata.py'])
            m_org.assert_called_once()
            p_get_json.assert_called_once()
