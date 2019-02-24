from pygitstory.github import Github
from pygitstory.gitlog_store import MongoGitlogStore
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
    gitlog_store = MongoGitlogStore(mongo_host, mongo_port, mongo_db)
    github = Github(repos_dir=repos_dir, gitlog_store=gitlog_store)
    history = github.get_history(args.url)
    for commit in history.commits:
        row = [str(e) for e in commit.__dict__.values()]
        print('\t'.join(row))

if __name__ == "__main__":
    execute()