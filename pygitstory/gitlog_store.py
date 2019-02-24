'''Git logs persistence.'''
from copy import deepcopy

from pymongo import MongoClient

from pygitstory.gitlog import GitCommit, GitLog

REPO_URL_FIELD = 'repo_url'

class MongoGitlogStore:
    """A store for Git logs in a Mongo DB."""

    def __init__(self, mongo_host, mongo_port, mongo_db):
        """Initialize the store for a given Mongo DB instance."""
        mongo_client = MongoClient(mongo_host, mongo_port)
        db = mongo_client[mongo_db]
        self.commits = db['commits']
    
    def get(self, repo_url):
        """
        Get the commit history of given remote repository.
        
        Arguments:
        repo_url -- the url of the repository.
        
        Return:
        a GitLog -- if it was found.
        None -- otherwise
        """
        commits = []
        for commit in self.commits.find({REPO_URL_FIELD: repo_url}):
            del commit['_id']
            del commit[REPO_URL_FIELD]
            commits.append(GitCommit(**commit))
        return GitLog(commits)
    
    def put(self, repo_url, gitlog):
        """
        Store the commit history of given remote repository.
        
        Arguments:
        repo_url -- the url of the repository;
        gitlog -- the commit history.
        """
        for commit in gitlog.commits:
            commit_doc = deepcopy(commit.__dict__)
            commit_doc[REPO_URL_FIELD] = repo_url
            self.commits.insert_one(commit_doc)
    
    def has(self, repo_url):
        """Check if a the commit history of a given repository was already stored."""
        return self.commits.find_one({REPO_URL_FIELD: repo_url}) is not None
