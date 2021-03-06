"""Git commit histories."""
from pygitstory.utils import as_datetime
class GitLog:
    """A git commit history."""

    def __init__(self, commits=[]):
        """Initialize a git commit history."""
        self.commits = commits
    
    def __eq__(self, value):
        return value.commits == self.commits

class GitCommit:
    """A git commit."""

    def __init__(self, sha, author_date, author_name, author_email,
                 commiter_date, commiter_name, commiter_email, message):
        """Initialize a commit."""
        self.sha = sha
        self.author_date = as_datetime(author_date)
        self.author_name = author_name
        self.author_email = author_email
        self.commiter_date = as_datetime(commiter_date)
        self.commiter_name = commiter_name
        self.commiter_email = commiter_email
        self.message = message

    def __eq__(self, other):
        return other.__dict__ == self.__dict__

    def __repr__(self):
        return str(self.__dict__)