import unittest
from unittest import mock
import fs


class TestFs(unittest.TestCase):
    @mock.patch('fs.parent_path', return_value='any/path/Testing')
    def test_001_parent_path(self, mock_check_output):
        path = fs.parent_path()
        folder = 'Testing'
        self.assertIn(folder, path)

    def test_002_parent_path(self):
        with mock.patch('fs.parent_path', return_value='my/path/Testing'):
            path = fs.parent_path() 
        folder = 'Testing'
        self.assertIn(folder, path)

    @mock.patch('fs.my_method')
    def test_004_my_method(self, mock_method):
        fs.my_method('name', 'version', 'sub_version')
        fs.my_method('name', 'version')
        self.assertTrue(mock_method.called)
