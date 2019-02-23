from os import path
from unittest import TestCase
from unittest.mock import patch, MagicMock
from pygitstory.gitrepo import GitRepo
from pygitstory.gitlog import GitLog
from pygitstory.tests.git_tests_log import REPO_PATH, REPO_URL, GIT_TEST_LOG

class TestGitRepo(TestCase):

    def setUp(self):
        self.repo = GitRepo(REPO_URL, REPO_PATH)
    
    @patch('pygitstory.gitrepo.clone', return_value="a log")
    def test_clone(self, clone_mock):
        self.repo.clone()
        clone_mock.assert_called_with(REPO_URL, REPO_PATH)

    @patch('pygitstory.gitrepo.log', return_value="a log")
    @patch('pygitstory.gitrepo.parse_log', return_value=GitLog(GIT_TEST_LOG))
    def test_log(self, parse_log_mock, log_mock):
        history = self.repo.log()
        log_mock.assert_called_with(REPO_PATH)
        parse_log_mock.assert_called_with('a log')
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
