from unittest import TestCase

from pygitstory.github import Github
from pygitstory.gitlog_store import MongoGitlogStore
from pygitstory.tests.git_tests_log import GIT_TEST_LOG, REPO_PATH, REPO_URL, REPOS_DIR

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'gitstory'

class TestCanViewGithubHistory(TestCase):

    def test_can_view_github_history(self):
        gitlog_store = MongoGitlogStore(MONGO_HOST, MONGO_PORT, MONGO_DB)
        # testing with non persisted log
        gitlog_store.commits.drop()
        github = Github(REPOS_DIR, gitlog_store)
        history = github.get_history(REPO_URL)
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
        # testing with persisted log
        history = github.get_history(REPO_URL)
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
