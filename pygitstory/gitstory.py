from pygitstory.github import Github
from pygitstory.gitlog_store import MongoGitlogStore
from pygitstory.exceptions import *

import os
from argparse import ArgumentParser


def execute():
    argparser = ArgumentParser('gistory', description='''
    A utility to get a Github repository commit history.''')
    argparser.add_argument('url', help='url of the github repository')
    args = argparser.parse_args()
    try: 
        mongo_host = os.environ['MONGO_HOST']
        mongo_port = int(os.environ['MONGO_PORT'])
        mongo_db = os.environ['MONGO_DB']
        repos_dir = os.environ['REPOS_DIR']
    except KeyError as e:
        argparser.error('Please set {} environment variable.'.format(str(e)))
    try:
        gitlog_store = MongoGitlogStore(mongo_host, mongo_port, mongo_db)
        github = Github(repos_dir=repos_dir, gitlog_store=gitlog_store)
        history = github.get_history(args.url)
    except Exception as err:
        if isinstance(err, RepoNotFound):
            argparser.error('Sorry, the repository does not exist.')
        elif isinstance(err, InvalidGitHost):
            argparser.error('Sorry, the repository url has an invalid host.')
        elif isinstance(err, InvalidReposDirectory):
            argparser.error('Sorry, the configured REPOS_DIR is not accessible.')
        else:
            argparser.error("Ups, I don't now what happened.")
            argparser.error("Blame the developer and forward him the following trace:")
            argparser.error(str(err))
    for commit in history.commits:
        row = [str(e) for e in commit.__dict__.values()]
        print('\t'.join(row))

if __name__ == "__main__":
    execute()