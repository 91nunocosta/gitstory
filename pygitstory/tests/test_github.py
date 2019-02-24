from unittest import TestCase
from unittest.mock import MagicMock, patch

from pygitstory import gitrepo
from pygitstory.gitrepo import GitLog
from pygitstory.github import Github

from pygitstory.tests.git_tests_log import REPO_URL, REPO_PATH, REPOS_DIR, GIT_TEST_LOG


class TestGithub(TestCase):

    def setUp(self):
        self.github = Github(REPOS_DIR)
        self.gitclone_patch = patch('pygitstory.github.GitRepo.clone')
        self.gitclone_mock = self.gitclone_patch.start()
        self.gitrepo_mock = MagicMock()
        self.gitclone_mock.return_value = self.gitrepo_mock
        self.gitrepo_mock.log.return_value = GitLog(GIT_TEST_LOG)

    def tearDown(self):
        self.gitclone_patch.stop()

    def test_get_history(self):
        history = self.github.get_history(REPO_URL)
        self.gitclone_mock.assert_called_with(REPO_URL, REPO_PATH)
        self.gitrepo_mock.log.assert_called()
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
