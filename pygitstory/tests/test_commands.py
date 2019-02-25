from subprocess import CompletedProcess, CalledProcessError
from unittest import TestCase
from unittest.mock import MagicMock, patch

from more_itertools.more import side_effect

from pygitstory.commands import *
from pygitstory.exceptions import *


class TestGitCommands(TestCase):

    @patch('pygitstory.commands.subprocess.run')
    @patch('pygitstory.commands.path_exists', return_value=False)
    def test_clone(self, exists_mock, run_mock):
        result = clone('url', 'dir')
        run_mock.assert_called()
        command_args = run_mock.call_args[0][0]
        self.assertListEqual(command_args, ['git', 'clone', 'url', 'dir'])
        self.assertTrue(result)

    @patch('pygitstory.commands.subprocess.run')
    @patch('pygitstory.commands.path_exists', return_value=True)
    def test_clone_does_nothing_when_cloned(self, exists_mock, run_mock):
        result = clone('url', 'dir')
        self.assertFalse(run_mock.called)
        self.assertFalse(result)

    @patch('pygitstory.commands.subprocess.run', side_effect=CalledProcessError(
        cmd=[],
        returncode=128,
        stderr=
        '''remote: Not Found
        fatal: repository 'https://github.com/a/' not found'''
    ))
    @patch('pygitstory.commands.path_exists', return_value=False)
    def test_clone_non_existing(self, exists_mock, run_mock):
        with self.assertRaises(RepoNotFound):
            clone('https://github.com/a/', 'dir')

    @patch('pygitstory.commands.subprocess.run', side_effect=CalledProcessError(
        cmd=[],
        returncode=128,
        stderr=
        '''fatal: unable to access 'https://invalidhost/': Could not resolve host: invalidhost'''
    ))
    @patch('pygitstory.commands.path_exists', return_value=False)
    def test_clone_invalid_git_host(self, exists_mock, run_mock):
        with self.assertRaises(InvalidGitHost):
            clone('https://invalidhost', 'dir')


    @patch('pygitstory.commands.subprocess.run', side_effect=CalledProcessError(
        cmd=[],
        returncode=128,
        stderr=
        '''fatal: could not create work tree dir '/a': Permission denied'''
    ))
    @patch('pygitstory.commands.path_exists', return_value=False)
    def test_clone_denied_repos_dir(self, exists_mock, run_mock):
        with self.assertRaises(InvalidReposDirectory):
            clone('host', 'denied_dir')

    @patch('pygitstory.commands.subprocess.run', side_effect=CalledProcessError(
        cmd=[],
        returncode=128,
        stderr=
        '''fatal: destination path '/' already exists and is not an empty directory.'''
    ))
    @patch('pygitstory.commands.path_exists', return_value=False)
    def test_clone_non_empty_repos_dir(self, exists_mock, run_mock):
        with self.assertRaises(InvalidReposDirectory):
            clone('host', 'non_empty_dir')

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
            'git', '--git-dir=path/.git', 'log', '--format=format:{}'.format(LOG_FORMAT), '--reverse'])
        self.assertEqual(output, 'output')
        print(LOG_FORMAT)
