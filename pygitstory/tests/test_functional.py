from unittest import TestCase

from pygitstory.gitrepo import GitRepo
from pygitstory.tests.git_tests_log import GIT_TEST_LOG, REPO_PATH, REPO_URL

class TestCanViewGithubHistory(TestCase):

    def test_can_view_github_history(self):
        repo = GitRepo(REPO_URL, REPO_PATH)
        repo.clone()
        history = repo.log()
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
