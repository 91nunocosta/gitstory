"""Git repositories."""
from pygitstory.gitlog import GitLog
from pygitstory.commands import log, clone
from pygitstory.parsing import parse_log


class GitRepo:
    """A git repository."""

    def __init__(self, remote_url, path):
        """
        Initialize a git repository for a given remote repository url.

        Arguments:
        remote_url -- URI of the remote repository.
        path -- the path for the directory where the repository was or will be cloned.
                Defaults to current working directory.
        """
        self.remote_url = remote_url
        self.path = path

    def clone(self):
        """Clone the git repository."""
        clone(self.remote_url, self.path)

    def log(self):
        """Get the repository commit history."""
        output = log(self.path)
        return parse_log(output)
