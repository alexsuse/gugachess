import unittest
from board import Piece, PieceType, PieceColor

class TestPiece(unittest.TestCase):
    def test_prints_pawn(self):
        p = Piece(PieceType.Pawn, PieceColor.White)
        self.assertEqual(p.__str__(), "op"

if __name__ == '__main__':
    unittest.main()
