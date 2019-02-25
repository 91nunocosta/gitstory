"""Exceptions."""
class RepoNotFound(Exception):
    """Exception raised when the passed remote git repository doesn't exist."""

    def __init__(self, url):
        self.url = url

class InvalidGitHost(Exception):
    """Exception raised when the passed remote git repository url has an invalid git host."""

    def __init__(self, url):
        self.url = url

class InvalidReposDirectory(Exception):
    """Exception raised when the passed repositories directory doesn't exist."""
    
    def __init__(self, directory, msg):
        self.directory = directory
