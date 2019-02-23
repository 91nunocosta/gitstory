"""Git repositories."""
from pygitstory.gitlog import GitLog


class GitRepo:
    """A git repository."""

    def __init__(self, remote_url, path=None):
        """
        Initialize a git repository for a given remote repository url.

        Arguments:
        remote_url -- URI of the remote repository.
        path -- the path for the directory where the repository was or will be cloned.
                Defaults to current working directory.
        """
        pass

    def clone(self):
        """
        Clone a git repository.

        Do nothing if the repository was already clone into the specified path.
        """
        pass

    def log(self):
        """Get the repository commit history."""
        return GitLog()
