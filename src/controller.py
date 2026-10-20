from collections.abc import Callable

from tic_tac_bot import TicTacBot
from tic_tac_toe import TicTacToe


class Controller:
    def __init__(
        self, game_state: TicTacToe, one_player_mode: bool , bot_player_symbol: int = TicTacToe.X
    ) -> None:
        self._original_game_state = game_state
        self._game_state = game_state
        self._bot = TicTacBot(game_state, bot_player_symbol)
        self._bot_player_symbol = bot_player_symbol
        self._one_player_mode = one_player_mode
        self._gs_change_callback = None

    def _start_game(self):
        if self._one_player_mode and self._bot_player_symbol == TicTacToe.X:
            row, col = self._bot.make_move()
            self._register_move(row, col)

    def _register_move(self, row: int, col: int) -> None:
        self._game_state = self._game_state.play(row, col)
        self._bot.record_move(self._game_state)
        self._handle_game_state_change()

    def set_game_state_change_callback(self, callback_function: Callable) -> None:
        self._gs_change_callback = callback_function
        self._start_game()

    def play(self, row: int, col: int) -> None:
        if (
            self._one_player_mode
            and self._game_state.get_current_turn() == self._bot_player_symbol
        ):
            return
        try:
            self._register_move(row, col)
            if (self._one_player_mode
                and not self._game_state.check_winner()
                and not self._game_state.is_tie()
                    ):
                self._bot_play()
        except ValueError as e:
            print(f"ValueError: {e}")
        except RuntimeError as e:
            print(f"RuntimeError {e}")

    def _bot_play(self):
        try:
            row, col = self._bot.make_move()
            self._register_move(row, col)
        except ValueError as e:
            print(f"ValueError: {e}")
        except RuntimeError as e:
            print(f"RuntimeError {e}")

    def check_winner(self) -> int | None:
        return self._game_state.check_winner()

    def is_tie(self) -> bool:
        return self._game_state.is_tie()

    def get_game_board(self) -> list[list[int]]:
        return self._game_state.get_board()

    def _handle_game_state_change(self) -> None:
        if self._gs_change_callback:
            self._gs_change_callback()

    def reset_game(self) -> None:
        self._game_state = self._original_game_state
        self._bot.reset()
        self._start_game()
        self._handle_game_state_change()
