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
    author_date_arg = 1
    committer_date_arg = 4
    commit_args[author_date_arg] = parse(commit_args[author_date_arg], ignoretz=True)
    commit_args[committer_date_arg] = parse(commit_args[committer_date_arg], ignoretz=True)
    return GitCommit(*commit_args)
