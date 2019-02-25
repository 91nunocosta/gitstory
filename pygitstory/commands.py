"""Git commands execution."""
import subprocess
from os import path
from os.path import exists as path_exists

from pygitstory.exceptions import (InvalidGitHost, InvalidReposDirectory,
                                   RepoNotFound)

# Log format:
# <hash> <author date> <author name> <author email> <commiter date> <commiter name> <commiter email> <message>
# dates are ISO 8601
#

# NOTE: this git log format does not ensure that the separator char doesn't occur inside the elements.
SEPARATOR = "*"
LOG_FORMAT = SEPARATOR.join(
    ['%H', '%aI', '%an', '%ae', '%cI', '%cn', '%ce', '%s'])


def clone(remote_url, path):
    """Clone a repository from a remote url into a given path."""
    if path_exists(path):
        return False
    try:
        __execute_git_command('clone', remote_url, path)
    except subprocess.CalledProcessError as err:
        if 'remote: Not Found' in err.stderr:
            raise RepoNotFound(remote_url)
        elif 'Could not resolve host' in err.stderr:
            raise InvalidGitHost(remote_url)
        elif 'Permission denied' in err.stderr or 'not an empty directory':
            raise InvalidReposDirectory(path, err.stderr)
        else:
            # unknown error
            # whenever someone gets here an new exception handling would be added
            raise err
    return True

# TODO: log error handling
def log(repo_path):
    """Log for a given git repository."""
    format_option = '--format=format:{}'.format(LOG_FORMAT)
    return __execute_git_command('log', format_option, '--reverse', git_repo_path=repo_path)

def __execute_git_command(command, *args, git_repo_path=None):
    cmd = ['git'] 
    if git_repo_path is not None:
        git_dir = path.join(git_repo_path, '.git')
        cmd.append('--git-dir={}'.format(git_dir))
    cmd.append(command)
    cmd += args
    result = subprocess.run(cmd, check=True, capture_output=True, encoding='utf-8')
    return result.stdout
