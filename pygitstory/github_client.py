'''Github public API.'''
import requests

from pygitstory.exceptions import RepoNotFound
from pygitstory.gitlog import GitCommit, GitLog

API_URL = 'https://api.github.com'

class GithubAPIClient:
    """A Github API client."""

    def get_history(self, repo):
        """Get the commit history of a given public Github repository using the Github API.
        
        Arguments:
        repo -- the GitHub repository, formatted as <owner>/<name>
        """
        url = '{}/repos{}/commits'.format(API_URL, repo)
        response = requests.get(url)
        if response.status_code == 404:
            raise RepoNotFound(url)
        response.raise_for_status()
        content = reversed(response.json())
        commits = [self.__parse_commit(commit) for commit in content]
        return GitLog(commits)

    def __parse_commit(self, commit_json):
        commit = commit_json['commit']
        author = commit['author']
        committer = commit['committer']
        return GitCommit(
            sha=commit_json['sha'], 
            author_date=author['date'], 
            author_name=author['name'], 
            author_email=author['email'],
            commiter_date=committer['date'], 
            commiter_name=committer['name'], 
            commiter_email=committer['email'], 
            message=commit['message']
        )
