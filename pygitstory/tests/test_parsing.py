import json
from os.path import abspath, dirname, join
from unittest import TestCase

from pygitstory.parsing import *

from pygitstory.tests.git_tests_log import GIT_TEST_LOG

GIT_LOG_OUTPUT_FILE = join(dirname(abspath(__file__)), 'git_tests_log.txt')

with open(GIT_LOG_OUTPUT_FILE, 'r') as git_log_file:
    GIT_LOG_OUTPUT = git_log_file.read()

class TestParsing(TestCase):

    def test_parse_log(self):
        history = parse_log(GIT_LOG_OUTPUT)
        self.assertListEqual(history.commits[:len(GIT_TEST_LOG)], GIT_TEST_LOG)
