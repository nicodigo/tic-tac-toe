class TicTacToe:
    X = 1
    O = -1
    EMPTY = 0

    def __init__(self):
        self._board: list[list[int]] = [[self.EMPTY] * 3 for _ in range(3)]
        self._turn: int = self.X
        self._winner = None

    def play(self, row: int, col: int) -> None:
        if row > 2 or col > 2:
            raise IndexError("error: play index out of bounds")
        if self._winner:
            return
        if self._board[row][col] != self.EMPTY:
            raise ValueError(f"error: the cell {row} {col} is not empty")

        self._board[row][col] = self._turn
        self._winner = self.check_winner()
        if self._turn == self.X:
            self._turn = self.O
        else:
            self._turn = self.X

    def check_winner(self) -> int | None:
        # check rows
        for row in self._board:
            if (
                row[0]
                == row[1]
                == row[2]
                != self.EMPTY
            ):
                return row[0]

        # check cols
        for i in range(3):
            if (
                self._board[0][i]
                == self._board[1][i]
                == self._board[2][i]
                != self.EMPTY
            ):
                return self._board[0][i]

        # check diagonals
        if (
            self._board[0][0]
            == self._board[1][1]
            == self._board[2][2]
            != self.EMPTY
        ):
            return self._board[1][1]

        if (
            self._board[0][2]
            == self._board[1][1]
            == self._board[2][0]
            != self.EMPTY
        ):
            return self._board[1][1]

        # There is no winner yet
        return None

    def is_board_complete(self) -> bool:
        for row in self._board:
            for cell in row:
                if cell == self.EMPTY:
                    return False
        return True

    def get_board(self) -> list[list[int]]:
        return [r.copy() for r in self._board]
