
class Board:
    def __init__(self, id):
        self._id = id
        self._board = [[None for i in range(8)] for i in range(8)]

    def Initialize(self):
        # set up a regular chess board
        pass

    @staticmethod
    def describe():
        return "describe"

    def AddPiece(self, position, piece):
        self._board[position[0]][position[1]] = piece

    def Move(self, src, dest):
        pass

    def IsValidMove(self, src, dest):
        if self._board[src[0]][src[1]] is None:
            return False
        if src == dest:
            return False
        if not self._board[src[0][1]].IsValidMoveForPiece(src, dest):
            return False
        # Insert more checks here (taking other piece, checking yourself...)
        return True

    def __str__(self):
        acc = ""
        for i, row in enumerate(self._board):
            for j, p in enumerate(row):
                if p is None:
                    #
                    if (i+j)%2:
                        acc += ".."
                    else:
                        acc += "##"
                else:
                    acc += p.__str__()
            acc += "\n"
        return acc
        #return "This will print a board"
