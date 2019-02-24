from unittest import TestCase

from pygitstory.github import Github
from pygitstory.tests.git_tests_log import GIT_TEST_LOG, REPO_PATH, REPO_URL, REPOS_DIR

class TestCanViewGithubHistory(TestCase):

    def test_can_view_github_history(self):
        github = Github(REPOS_DIR)
        history = github.get_history(REPO_URL)
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
