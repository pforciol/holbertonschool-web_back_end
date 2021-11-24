#!/usr/bin/env python3
"""Testing functions in client.py"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_obj = GithubOrgClient(org_name)
        url = f"https://api.github.com/orgs/{org_name}"

        self.assertEqual(test_obj.org, {'key': 'value'})
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one based
        on the mocked payload"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://nowhere.com"}
            test_obj = GithubOrgClient('foo')
            self.assertEqual(test_obj._public_repos_url,
                             "https://nowhere.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """public_repos unit test
        - list of repos is what you expect from the chosen payload
        - mocked property and the mocked get_json was called once"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:

            payload = {'login': 'microsoft',
                       'id': 6154722,
                       'node_id': 'MDEyOk9yZ2FuaXphdGlvbjYxNTQ3MjI=',
                       'url': 'https://api.github.com/orgs/microsoft',
                       'repos_url':
                       'https://api.github.com/orgs/microsoft/repos'}

            test_object = GithubOrgClient('foo')
            mock_get_json.return_value = payload
            org = test_object.org
            mock_public_repos_url.return_value = org.get('repos_url')

            self.assertEqual(test_object._public_repos_url,
                             'https://api.github.com/orgs/microsoft/repos')
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """has_license unit-test"""
        test_object = GithubOrgClient('foo')
        self.assertEqual(test_object.has_license(repo, license_key), expected)

        with self.assertRaises(AssertionError):
            test_object.has_license(repo, None)


@parameterized_class([{"org_payload": TEST_PAYLOAD[0][0],
                       "repos_payload": TEST_PAYLOAD[0][1],
                       "expected_repos": TEST_PAYLOAD[0][2],
                       "apache2_repos": TEST_PAYLOAD[0][3]}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """GithubOrgClient.public_repos integration tests"""
    @classmethod
    def setUpClass(cls):
        """mock request.get to return example payloads found in the fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.get_patcher.side_effect = cls.repos_payload

        cls.org_patcher = patch('client.GithubOrgClient.org',
                                side_effect=cls.get_patcher)

        cls.public_repos_url_patcher = patch("client.GithubOrgClient"
                                             "._public_repos_url",
                                             return_value=cls.org_payload
                                             .get('repos_url'))

        cls.get_patcher.start()
        cls.org_patcher.start()
        cls.public_repos_url_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stops the patcher"""
        cls.get_patcher.stop()
        cls.org_patcher.stop()
        cls.public_repos_url_patcher.stop()

    def test_public_repos(self):
        """public_repos unit test"""
        test_obj = GithubOrgClient('foo')
        self.assertEqual(test_obj._public_repos_url.return_value,
                         self.org_payload.get('repos_url'))

    def test_public_repos_with_license(self):
        '''Tests public_repos method with the argument license="apache-2.0"'''
        test_obj = GithubOrgClient('foo')
