from hello import HelloTest
import unittest
from unittest import mock

class TestFoo(unittest.TestCase):

    @mock.patch('hello.HelloTest.foo')
    def test_foo_case(self, mock_foo):

        ht = HelloTest.foo("some string")
        self.assertTrue(mock_foo.called)
        self.assertEqual(mock_foo.call_args[0][0], "some string")