'''Git logs persistence.'''
from pymongo import MongoClient

from pygitstory.gitlog import GitLog, GitCommit

class MongoGitlogStore:
    """A store for Git logs in a Mongo DB."""

    def __init__(self, mongo_host, mongo_port, mongo_db):
        """Initialize the store for a given Mongo DB instance."""
        pass
    
    def get(self, repo_url):
        """
        Get the commit history of given remote repository.
        
        Arguments:
        repo_url -- the url of the repository.
        
        Return:
        a GitLog -- if it was found.
        None -- otherwise
        """
        return GitLog()
    
    def put(self, repo_url, gitlog):
        """
        Store the commit history of given remote repository.
        
        Arguments:
        repo_url -- the url of the repository;
        gitlog -- the commit history.
        """
        pass
    
    def has(self, repo_url):
        """Check if a the commit history of a given repository was already stored."""
        return False