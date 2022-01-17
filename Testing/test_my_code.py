import unittest
from my_code import MyCode


class TestMyCode(unittest.TestCase):
    def test_001_add(self):
        result = MyCode.add(2, 1)
        self.assertEqual(3, result)