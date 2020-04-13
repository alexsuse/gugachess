import unittest
from board import Board

class TestBoard(unittest.TestCase):
  def test_prints(self):
    b = Board()
    self.assertEqual(b.__str__(), "This will print a board")

if __name__ == '__main__':
  unittest.main()
