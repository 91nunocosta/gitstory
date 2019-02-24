"""Github API."""
from os.path import basename, join

from urllib.parse import urlparse

from pygitstory.gitrepo import GitRepo
from pygitstory.gitlog import GitLog


class Github:
    """An API for Github."""

    def __init__(self, repos_dir):
        self.repos_dir = repos_dir

    def get_history(self, repo_url):
        """
        Get the commit history of a GitHub remote repository.

        Arguments:
        repo_url -- the url of the remote  GitHub repository.
        """
        repo_path = self.__repo_path(repo_url)
        repo = GitRepo.clone(repo_url, repo_path)
        return repo.log()

    def __repo_path(self, repo_url):
        repo_name = basename((urlparse(repo_url).path))
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        return join(self.repos_dir, repo_name)
