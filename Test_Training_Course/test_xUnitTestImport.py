import unittest
import zutesten1


class TestKlasse(unittest.TestCase):
   def test_gerade(self):
      self.assertLess(zutesten1.zahlen(),0.5)


if __name__ == '__main__':
   unittest.main()
