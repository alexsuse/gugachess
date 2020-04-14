import enum

# pawn is 1, bishop is 2 ....

class PieceType(enum.Enum):
    Pawn = 1
    Bishop = 2
    Knight = 3
    Rook = 4
    Queen = 5
    King = 6

_PIECE_TYPE_STRINGS = {
    PieceType.Pawn: "p",
    PieceType.Bishop: "b",
    PieceType.Knight: "n",
    PieceType.Rook:"r",
    PieceType.Queen: "q",
    PieceType.King: "k",
}

class PieceColor(enum.Enum):
    Black = 1
    White = 2

_PIECE_COLOR_STRINGS = {
    PieceColor.Black: "*",
    PieceColor.White: "o",
}

def isValidForPawn(src, dest, color):
    # TODO(susemihl): implement
    return False

def isValidForBishop(src, dest, color):
    # TODO(susemihl): implement
    return False

def isValidForKnight(src, dest, color):
    # TODO(susemihl): implement
    return False


def isValidForQueen(src, dest, color):
    # TODO(susemihl): implement
    return False

def isValidForRook(src, dest, color):
    # TODO(susemihl): implement
    return False

def isValidForKing(src, dest, color):
    # TODO(susemihl): implement
    return False

_PIECE_TYPE_MOVE_VALIDATORS = {
    PieceType.Pawn: isValidForPawn,
    PieceType.Bishop: isValidForBishop,
    PieceType.Knight: isValidForKnight,
    PieceType.Rook: isValidForRook,
    PieceType.Queen: isValidForQueen,
    PieceType.King: isValidForKing,
}

class Piece:
    # Every Piece needs a color
    def __init__(self, type, color):
        self._type = type
        self._color = color

    # IsValidMoveForPiece veriefies that in an empty board
    # the piece of this type and color can move from src to
    # dest. This does NOT mean that this is a valid move
    # in the context of the game (the move might be towards
    # an occupied position, or it might set yourself in check)
    def IsValidMoveForPiece(self, src, dest):
        return _PIECE_TYPE_MOVE_VALIDATORS[self._type](src, dest, self._color)
        # if other types
        return True

    def __str__(self):
        return _PIECE_COLOR_STRINGS[self._color] + _PIECE_TYPE_STRINGS[self._type]
