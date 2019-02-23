"""Git commands output parsing."""

from pygitstory.gitlog import GitCommit, GitLog

def parse_log(log_output):
    """Parse git log command output."""
    return GitLog()
