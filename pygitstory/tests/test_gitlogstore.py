from copy import deepcopy
from unittest import TestCase
from dateutil.parser import parse

from pygitstory.gitlog import GitLog
from pygitstory.gitlog_store import REPO_URL_FIELD, MongoGitlogStore
from pygitstory.tests.git_tests_log import (GIT_TEST_LOG, REPO_PATH, REPO_URL,
                                            REPOS_DIR)

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'gitstory'

TARGET_REPO = 'https://github.com/example/target-repo.git'
OTHER_REPO = 'https://github.com/example/other-repo.git'
COMMITS = [
    {
        REPO_URL_FIELD: TARGET_REPO,
        "sha": "15c8c55ea88e9d2e3b2f975cc8eef30848080b7f",
        "author_date": "2018-06-08 13:56:25Z",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 13:56:25Z",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "first commit"
    },
    {
        REPO_URL_FIELD: TARGET_REPO,
        "sha": "00a5762b09a7704aef6e30ccd7c368758a56261a",
        "author_date": "2018-06-08 13:59:55Z",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 13:59:55Z",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Add a file"
    },
    {
        REPO_URL_FIELD: TARGET_REPO,
        "sha": "57012cdf0c3b277ba2feef552ab60d58f13bf774",
        "author_date": "2018-06-08 14:00:27Z",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 14:00:27Z",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Rename a file"
    },
    {
        REPO_URL_FIELD: OTHER_REPO,
        "sha": "5e013cdf0c3bds77ba4feef552af60d58f13bf774",
        "author_date": "2018-06-08 14:00:27Z",
        "author_name": "Johann Egger",
        "author_email": "johann@codacy.com",
        "commiter_date": "2018-06-08 14:00:27Z",
        "commiter_name": "Johann Egger",
        "commiter_email": "johann@codacy.com",
        "message": "Something"
    }
]

TARGET_HISTORY = GIT_TEST_LOG


class TestMongoGitlogStore(TestCase):

    def setUp(self):
        self.gitlog_store = MongoGitlogStore(MONGO_HOST, MONGO_PORT, MONGO_DB)
        self.gitlog_store.commits.drop()

    def test_get(self):
        self.gitlog_store.commits.insert_many(deepcopy(COMMITS))
        history = self.gitlog_store.get(TARGET_REPO)
        self.maxDiff = None
        self.assertListEqual(history.commits, TARGET_HISTORY)

    def test_put(self):
        self.gitlog_store.put(TARGET_REPO, GitLog(GIT_TEST_LOG))
        found_commits = list(self.gitlog_store.commits.find(
            {REPO_URL_FIELD: TARGET_REPO}))
        for commit in found_commits:
            # _id is a Mongo added key
            del commit['_id']
        # 4th commit is the only one from other repo
        self.maxDiff = None
        expected_commits = deepcopy(COMMITS[:3])
        for commit in expected_commits:
            # date fields are stored in Mongo as strings not datetime
            commit['author_date'] = parse(commit['author_date']).replace(tzinfo=None)
            commit['commiter_date'] = parse(commit['commiter_date']).replace(tzinfo=None)
        self.assertListEqual(found_commits, expected_commits)

    def test_has(self):
        self.assertFalse(self.gitlog_store.has(TARGET_REPO))
        self.gitlog_store.commits.insert_many(deepcopy(COMMITS))
        self.assertTrue(self.gitlog_store.has(TARGET_REPO))
