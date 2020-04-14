import unittest
from board import Board

class TestBoard(unittest.TestCase):
    def test_prints(self):
        b = Board("my board")
        self.assertEqual(b.__str__(), "my board")

    def test_describe(self):
        self.assertEqual(Board.describe(), "describe")

    def test_cannot_move_empty_position(self):
        b = Board("my board")
        self.assertFalse(b.IsValidMove((0,0), (1,1)))

    def test_cannot_move_to_same_position(self):
        b = Board("my board")
        b.AddPiece((0,0), "a")
        b.AddPiece((10,10), "b")
        self.assertFalse(b.IsValidMove((0,0), (0,0)))



if __name__ == '__main__':
    unittest.main()
