from os.path import join, abspath, dirname, exists

from pygitstory.tests.git_tests_log import REPO_PATH, REPO_URL
from pygitstory.commands import log, clone

if __name__ == "__main__":
    if not exists(REPO_PATH):
        clone(REPO_URL, REPO_PATH)
    log_output_file_path = join(dirname(abspath(__file__)), 'git_tests_log.txt')
    with open(log_output_file_path, 'w') as log_output_file:
        result = log(REPO_PATH)     
        log_output_file.write(result)
