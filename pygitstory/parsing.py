"""Git commands output parsing."""

from dateutil.parser import parse

from pygitstory.gitlog import GitCommit, GitLog
from pygitstory.commands import SEPARATOR

def parse_log(log):
    """Parse git log command output."""
    commits = []
    for line in log.splitlines(keepends=False):
        commit = __parse_commit(line)
        commits.append(commit)
    return GitLog(commits)

def __parse_commit(line):
    commit_args = line.split(SEPARATOR)
    return GitCommit(*commit_args)
