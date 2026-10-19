from tic_tac_toe import TicTacToe


class GSNode:
    def __init__(self, game_state: TicTacToe) -> None:
        self.game_state = game_state
        self.value = 0
        self.next_moves: list[GSNode] | None = None


class TicTacBot():
    def __init__(self, game_state: TicTacToe) -> None:
        self._game_state = game_state
        self._root = GSNode(game_state)
