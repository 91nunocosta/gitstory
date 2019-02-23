"""Git commit histories."""


class GitLog:
    """A git commit history."""

    def __init__(self, commits=[]):
        """Initialize a git commit history."""
        self.commits = commits

class GitCommit:
    """A git commit."""

    def __init__(self, sha, author_date, author_name, author_email,
                 commiter_date, commiter_name, commiter_email, message):
        """Initialize a commit."""
        self.sha = sha
        self.author_date = author_date
        self.author_name = author_name
        self.author_email = author_email
        self.commiter_date = commiter_date
        self.commiter_name = commiter_name
        self.commiter_email = commiter_email
        self.message = message

    def __eq__(self, other):
        return other.__dict__ == self.__dict__

    def __repr__(self):
        return str(self.__dict__)