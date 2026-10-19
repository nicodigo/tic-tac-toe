from tkinter import Button, E, Frame, Label, N, S, StringVar, Tk, W

from board_tile_gui import BoardTileGUI
from tic_tac_toe import TicTacToe


class TicTacToeGUI:
    def __init__(self, root: Tk, game_board: TicTacToe) -> None:
        self._game_board = game_board
        self._game_board.__init__()
        root.title("Tic-Tac-Toe")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        self._mainframe = Frame(root)
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._mainframe.grid_columnconfigure(0, weight=3)
        self._mainframe.grid_rowconfigure(0, weight=16)
        self._mainframe.grid_rowconfigure(1, weight=1)

        self._board = Frame(self._mainframe)
        self._board.configure(bg="#222233")
        self._board.grid(column=0, row=0, sticky=(N, W, E, S))
        self._board.grid_columnconfigure([0, 1, 2], weight=1)
        self._board.grid_rowconfigure([0, 1, 2], weight=1)

        self._tiles: list[BoardTileGUI] = []
        padx = 5
        pady = 5
        for i in range(3):
            for j in range(3):
                new_tile = BoardTileGUI(i, j, 128, self._board)
                new_tile.grid(row=i, column=j, sticky=(N, W, E, S))
                new_tile.configure(bg="white")

                if i == 0:
                    new_tile.grid_configure(pady=(0, pady))
                elif i == 2:
                    new_tile.grid_configure(pady=(pady, 0))
                else:
                    new_tile.grid_configure(pady=pady)

                if j == 0:
                    new_tile.grid_configure(padx=(0, padx))
                elif j == 2:
                    new_tile.grid_configure(padx=(padx, 0))
                else:
                    new_tile.grid_configure(padx=padx)

                self._tiles.append(new_tile)

                new_tile.bind(
                    "<Button-1>", lambda e, tile=new_tile: self._tile_clicked(tile)
                )

        self._lower_section = Frame(self._mainframe)
        self._lower_section.grid_columnconfigure(0, weight=1)
        self._lower_section.grid_columnconfigure(1, weight=1)
        self._lower_section.grid_rowconfigure(0, weight=1)
        self._lower_section.grid(row=1, column=0, sticky=(N, W, E, S))
        self._lower_section.configure(bg="#536878")
        reset_btn = Button(self._lower_section)
        reset_btn.configure(
            command=lambda r=root, g=self._game_board: self.__init__(r, g),
            text="Reset Game Board",
        )
        reset_btn.grid(column=0, row=1, padx=20, pady=20, sticky=W)
        self._style_button(reset_btn)
        exit_btn = Button(self._lower_section)
        exit_btn.configure(command=root.destroy, text="EXIT")
        exit_btn.grid(column=1, row=1, padx=20, pady=20, sticky=E)
        self._style_button(exit_btn)

        self._winner_value = StringVar(value="")
        winner_banner = Label(self._lower_section, textvariable=self._winner_value)
        winner_banner.grid(column=0, row=0, columnspan=2, sticky=(N, E, S, W))
        winner_banner.configure(font=("Arial", 48), bg="#536878")

    def _style_button(self, b: Button) -> None:
        b.configure(
            background="#98817b",
            border=0.0,
            highlightthickness=0,
            foreground="#222233",
            takefocus=False,
        )

    def _tile_clicked(self, tile: BoardTileGUI) -> None:
        row = tile.get_row()
        col = tile.get_col()
        print(f"Clicked: row={row} col={col}")
        self._play(row, col)

    def _play(self, row: int, col: int) -> None:
        try:
            self._game_board.play(row, col)
            self._draw_board()
            winner = self._game_board.check_winner()
            if winner:
                self._handle_winner(winner)
            print("succesful play")
        except ValueError as e:
            print(f"ValueError: {e}")
        except RuntimeError as e:
            print(f"RuntimeError {e}")

    def _draw_board(self) -> None:
        i = 0
        for row in self._game_board.get_board():
            for cell in row:
                tile = self._tiles[i]
                if cell == TicTacToe.X:
                    tile.set_text("X")
                elif cell == TicTacToe.O:
                    tile.set_text("O")
                else:
                    tile.set_text()
                i += 1

    def _handle_winner(self, winner: int) -> None:
        if winner == TicTacToe.X:
            self._winner_value.set("Player (X) has Won!")
        elif winner == TicTacToe.O:
            self._winner_value.set("Player (O) has Won!")
