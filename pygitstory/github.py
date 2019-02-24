"""Github API."""
from os.path import basename, join

from urllib.parse import urlparse

from pygitstory.gitrepo import GitRepo
from pygitstory.gitlog import GitLog

class Github:
    """An API for Github."""

    def __init__(self, repos_dir, gitlog_store):
        self.repos_dir = repos_dir
        self.gitlog_store = gitlog_store

    def get_history(self, repo_url):
        """
        Get the commit history of a GitHub remote repository.

        Arguments:
        repo_url -- the url of the remote  GitHub repository.
        """
        repo_path = self.__repo_path(repo_url)
        if self.gitlog_store.has(repo_url):
            return self.gitlog_store.get(repo_url)
        else:
            repo = GitRepo.clone(repo_url, repo_path)
            log = repo.log()
            self.gitlog_store.put(repo_url, log)
            return log

    def __repo_path(self, repo_url):
        repo_name = basename((urlparse(repo_url).path))
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        return join(self.repos_dir, repo_name)
