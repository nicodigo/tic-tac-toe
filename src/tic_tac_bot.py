from tic_tac_toe import TicTacToe


class GSNode:
    def __init__(
        self, game_state: TicTacToe, move: tuple[int, int] | None = None
    ) -> None:
        self.game_state = game_state
        self.move: tuple[int, int] | None = move
        self.next_states: list[GSNode] | None = None
        self.depth = 0

    def __repr__(self) -> str:
        return f"Move: {self.move} Depth: {self.depth}"


class TicTacBot:
    def __init__(self, game_state: TicTacToe) -> None:
        self._tree_root: GSNode = GSNode(game_state)
        self._tree_root = self._build_tree(self._tree_root)
        self._root = self._tree_root

    def reset(self):
        self._root = self._tree_root

    def make_move(self) -> tuple[int, int]:
        if self._root.next_states == None:
            raise RuntimeError("error: there is not possible moves")

        if self._root.game_state.is_first_move():
            return (1, 1)

        max_node = None
        min_value = -10
        for node in self._root.next_states:
            value = self._calculate_minmax(node, self._root.game_state.get_current_turn(), True)
            if value > min_value:
                max_node = node
                min_value = value

        if max_node and max_node.move:
            return max_node.move

        raise RuntimeError("error: something went wrong making move")

    def _calculate_minmax(self, root: GSNode, symbol: int, minimize=True) -> int:
        if root.next_states == None:
            if root.game_state.check_winner() == symbol:
                return 1
            elif root.game_state.is_tie():
                return 0
            else:
                return -1
        if minimize:
            value = 10
            for node in root.next_states:
                value = min(value, self._calculate_minmax(node, symbol, False))
            return value
        else:
            value = -10
            for node in root.next_states:
                value = max(value, self._calculate_minmax(node, symbol, True))
            return value

    def record_move(self, game_state: TicTacToe) -> None:
        if self._root.next_states == None:
            self._root = GSNode(game_state)
            self._build_tree(self._root)
            return

        for node in self._root.next_states:
            if game_state == node.game_state:
                self._root = node
                return

        self._root = GSNode(game_state)
        self._build_tree(self._root)
        return

    def _build_tree(self, root: GSNode, depth=0) -> GSNode:
        legal_moves = root.game_state.get_legal_moves()
        if len(legal_moves) == 0:
            root.next_states = None
            root.depth = depth
            return root

        root.next_states = []
        for row, col in legal_moves:
            new_game_state = root.game_state.play(row, col)
            new_node = GSNode(new_game_state, (row, col))
            root.next_states.append(self._build_tree(new_node, depth + 1))
            root.depth = depth

        return root
