from os.path import abspath, join, dirname
from pygitstory.gitlog import GitCommit
from datetime import datetime, timezone, timedelta

from dateutil.tz import UTC

TIMEZONE = UTC

REPO_NAME = 'codacy/git-tests'
REPO_URL = 'https://github.com/{}.git'.format(REPO_NAME)
REPOS_DIR = join(dirname(abspath(__file__)), 'tmp') 
REPO_PATH = join(REPOS_DIR, 'git-tests')

# first 3 commits from 'https://github.com/codacy/git-tests.git'
GIT_TEST_LOG = [
    GitCommit(
        sha='15c8c55ea88e9d2e3b2f975cc8eef30848080b7f',
        author_date=datetime(2018, 6, 8, 13, 56, 25, tzinfo=TIMEZONE),
        author_name="Johann Egger",
        author_email="johann@codacy.com",
        commiter_date=datetime(2018, 6, 8, 13, 56, 25, tzinfo=TIMEZONE),
        commiter_name="Johann Egger",
        commiter_email="johann@codacy.com",
        message="first commit"
    ),
    GitCommit(
        sha='00a5762b09a7704aef6e30ccd7c368758a56261a',
        author_date=datetime(2018, 6, 8, 13, 59, 55, tzinfo=TIMEZONE),
        author_name="Johann Egger",
        author_email="johann@codacy.com",
        commiter_date=datetime(2018, 6, 8, 13, 59, 55, tzinfo=TIMEZONE),
        commiter_name="Johann Egger",
        commiter_email="johann@codacy.com",
        message="Add a file"
    ),
    GitCommit(
        sha='57012cdf0c3b277ba2feef552ab60d58f13bf774',
        author_date=datetime(2018, 6, 8, 14, 0, 27, tzinfo=TIMEZONE),
        author_name="Johann Egger",
        author_email="johann@codacy.com",
        commiter_date=datetime(2018, 6, 8, 14, 0, 27, tzinfo=TIMEZONE),
        commiter_name="Johann Egger",
        commiter_email="johann@codacy.com",
        message="Rename a file"
    ),
]
