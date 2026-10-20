class TicTacToe:
    X = 1
    O = 2
    EMPTY = 0

    def __init__(self, board: list[list[int]] | None = None, turn: int = X):
        if board is None:
            self._board: list[list[int]] = [[self.EMPTY] * 3 for _ in range(3)]
        else:
            self._board = board
        self._turn: int = turn
        self._winner = None
        self._winner = self.check_winner()

    def play(self, row: int, col: int) -> 'TicTacToe':
        if row > 2 or col > 2:
            raise IndexError("error: play index out of bounds")
        if self._winner:
            raise RuntimeError(f"error: player {self._winner} has already won")
        if self._board[row][col] != self.EMPTY:
            raise ValueError(f"error: the cell {row} {col} is not empty")

        new_board = self.get_board()
        new_board[row][col] = self._turn
        if self._turn == self.X:
            turn = self.O
        else:
            turn = self.X
        return TicTacToe(new_board, turn)

    def check_winner(self) -> int | None:
        if self._winner:
            return self._winner
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

    def _is_board_complete(self) -> bool:
        for row in self._board:
            for cell in row:
                if cell == self.EMPTY:
                    return False
        return True

    def get_board(self) -> list[list[int]]:
        return [r.copy() for r in self._board]

    def is_tie(self) -> bool:
        return self._is_board_complete() and (self._winner == None)

    def get_legal_moves(self) -> list[tuple[int, int]]:
        if self._winner:
            return []
        legal_moves: list[tuple[int,int]] = []
        for r in range(3):
            for c in range(3):
                if self._board[r][c] == self.EMPTY:
                    legal_moves.append((r,c))
        return legal_moves

    def get_current_turn(self) -> int:
        return self._turn

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TicTacToe):
            return False

        if self._turn != other.get_current_turn():
            return False

        other_board = other.get_board()
        for r in range(3):
            for c in range(3):
                if self._board[r][c] != other_board[r][c]:
                    return False

        return True

    def is_first_move(self):
        for row in self._board:
            for cell in row:
                if cell != self.EMPTY:
                    return False
        return True

