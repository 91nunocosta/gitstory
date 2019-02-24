from unittest import TestCase

from pygitstory.gitlog_store import MongoGitlogStore

from pygitstory.tests.git_tests_log import GIT_TEST_LOG, REPOS_DIR, REPO_PATH, REPO_URL


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'gitstory'

TARGET_REPO = 'https://github.com/example/target-repo.git'
OTHER_REPO = 'https://github.com/example/other-repo.git'
COMMITS = [
    {
        "repo_url": TARGET_REPO,
        "sha": "15c8c55ea88e9d2e3b2f975cc8eef30848080b7f",
        "author_date": "2018-06-08 15:56:25",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 15:56:25",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "first commit"
    },
    {
        "repo_url": TARGET_REPO,
        "sha": "00a5762b09a7704aef6e30ccd7c368758a56261a",
        "author_date": "2018-06-08 15:59:55",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 15:59:55",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Add a file"
    },
    {
        "repo_url": TARGET_REPO,
        "sha": "57012cdf0c3b277ba2feef552ab60d58f13bf774",
        "author_date": "2018-06-08 16:00:27",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 16:00:27",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Rename a file"
    },
    {
        "repo_url": OTHER_REPO,
        "sha": "57012cdf0c3b277ba2feef552ab60d58f13bf774",
        "author_date": "2018-06-08 16:00:27",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 16:00:27",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Rename a file"
    }
]

TARGET_HISTORY = GIT_TEST_LOG


class TestMongoGitlogStore(TestCase):

    def setUp(self):
        self.gitlog_store = MongoGitlogStore(MONGO_HOST, MONGO_PORT, MONGO_DB)
        self.gitlog_store.commits.drop()

    def test_get(self):
        self.gitlog_store.commits.insert_many(COMMITS)
        history = self.gitlog_store.get(TARGET_REPO)
        self.maxDiff = None
        self.assertListEqual(history.commits, TARGET_HISTORY)

    def test_put(self):
        pass

    def test_has(self):
        pass
