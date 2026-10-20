from tic_tac_toe import TicTacToe


class GSNode:
    def __init__(self, game_state: TicTacToe, move: tuple[int, int] | None = None) -> None:
        self.game_state = game_state
        self.value = 0
        self.move: tuple[int, int] | None = move
        self.next_states: list[GSNode] | None = None
    def __repr__(self) -> str:
        return f"Move: {self.move} Value: {self.value}"


class TicTacBot:
    def __init__(self, game_state: TicTacToe, playing: int) -> None:
        self._player = playing
        self._root: GSNode = GSNode(game_state)
        self._root = self._build_tree(self._root)

    def make_move(self) -> tuple[int, int] | None:
        if self._root.game_state.get_current_turn() != self._player:
            raise RuntimeError("error: not my turn")
        if self._root.next_states == None:
            raise RuntimeError("error: there is not possible moves")
        if self._root.game_state.is_first_move():
            return (1,1)
        self._calculate_minmax(self._root)
        print(f"after minmax root: {self._root} value: {self._root.value} next_states: {self._root.next_states}")
        for node in self._root.next_states:
            if node.value == self._root.value:
                return node.move

    def _calculate_minmax(self, root: GSNode, minimize=False) -> int:
        if root.next_states == None:
            if root.game_state.check_winner() == self._player:
                root.value = 1
            elif root.game_state.is_tie():
                root.value = 0
            else:
                root.value = -1
            return root.value
        if minimize:
            value = 10
            for node in root.next_states:
                value = min(value, self._calculate_minmax(node, False))
            root.value = value
            return value
        else:
            value = -10
            for node in root.next_states:
                value = max(value, self._calculate_minmax(node, True))
            root.value = value
            return value


    def record_move(self, game_state: TicTacToe) -> None:
        if self._root.next_states == None:
            self._root = GSNode(game_state)
            self._build_tree(self._root)
            return

        for node in self._root.next_states:
            if game_state == node.game_state:
                node.move = None
                self._root = node
                return

        self._root = GSNode(game_state)
        self._build_tree(self._root)
        return



    def _build_tree(self, root: GSNode) -> GSNode:
        legal_moves = root.game_state.get_legal_moves()
        if len(legal_moves) == 0:
            root.next_states = None
            return root

        root.next_states = []
        for row, col in legal_moves:
            new_game_state = root.game_state.play(row, col)
            new_node = GSNode(new_game_state, (row, col))
            root.next_states.append(self._build_tree(new_node))

        return root


