import json
import requests
from os.path import join, abspath, dirname

from unittest import TestCase
from unittest.mock import patch, MagicMock

from pygitstory.tests.git_tests_log import REPO_URL, GIT_TEST_LOG, REPO_NAME
from pygitstory.github_client import GithubAPIClient

from pygitstory.exceptions import *

def read_from_json(file_path):
    with open(file_path, 'r') as json_file:
        return json.loads(json_file.read())

RESPONSE_JSON_FILE = join(dirname(abspath(__file__)), 'git_test_log_commits_api_response.json')

RESPONSE_EXAMPLE= read_from_json(RESPONSE_JSON_FILE)

class TestGithubAPIClient(TestCase):

    def setUp(self):
        self.github_client = GithubAPIClient()

    @patch('pygitstory.github_client.requests.get')
    def test_get_history(self, requests_get_mock):
        requests_get_mock.return_value.json.return_value = RESPONSE_EXAMPLE
        history = self.github_client.get_history(REPO_NAME)
        requests_get_mock.assert_called_with('https://api.github.com/repos/codacy/git-tests/commits')
        self.maxDiff = None
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)

    @patch('pygitstory.github_client.requests.get')
    def test_get_history_not_found_repo(self, requests_get_mock):
        requests_get_mock.return_value.status_code = 404
        with self.assertRaises(RepoNotFound):
            self.github_client.get_history(REPO_NAME)
