from unittest import TestCase
from unittest.mock import patch, MagicMock
from subprocess import CompletedProcess

from pygitstory.commands import * 

class TestGitCommands(TestCase):

    @patch('pygitstory.commands.subprocess.run')
    def test_clone(self, run_mock):
        clone('url', 'dir')
        run_mock.assert_called()
        command_args = run_mock.call_args[0][0]
        self.assertListEqual(command_args, ['git', 'clone', 'url', 'dir'])

    @patch('pygitstory.commands.subprocess.run', return_value=CompletedProcess(
        args=[], 
        returncode=0,
        stdout='output')
    )
    def test_log(self, run_mock):
        output = log('path')
        run_mock.assert_called()
        command_args = run_mock.call_args[0][0]
        self.assertListEqual(command_args, [
            'git', '--git-dir=path/.git', 'log', '--format=format:{}'.format(LOG_FORMAT)])
        self.assertEqual(output, 'output')
        print(LOG_FORMAT)
