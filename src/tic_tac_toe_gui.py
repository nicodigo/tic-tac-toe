from tkinter import Button, E, Frame, Label, N, S, StringVar, Tk, W

from board_tile_gui import BoardTileGUI
from controller import Controller
from tic_tac_toe import TicTacToe


class TicTacToeGUI:
    def __init__(
        self,
        root: Tk,
        controller: Controller
    ) -> None:
        self._controller = controller
        root.title("Tic-Tac-Toe")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        mainframe = Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.grid_columnconfigure(0, weight=3)
        mainframe.grid_rowconfigure(0, weight=16)
        mainframe.grid_rowconfigure(1, weight=1)

        board = Frame(mainframe)
        board.configure(bg="#222233")
        board.grid(column=0, row=0, sticky=(N, W, E, S))
        board.grid_columnconfigure([0, 1, 2], weight=1)
        board.grid_rowconfigure([0, 1, 2], weight=1)

        self._tiles: list[BoardTileGUI] = []
        padx = 5
        pady = 5
        for i in range(3):
            for j in range(3):
                new_tile = BoardTileGUI(i, j, 128, board)
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

        lower_section = Frame(mainframe)
        lower_section.grid_columnconfigure(0, weight=1)
        lower_section.grid_columnconfigure(1, weight=1)
        lower_section.grid_rowconfigure(0, weight=1)
        lower_section.grid(row=1, column=0, sticky=(N, W, E, S))
        lower_section.configure(bg="#536878")
        reset_btn = Button(lower_section)
        reset_btn.configure(
            command=self._reset_game,
            text="Reset Game Board",
        )
        reset_btn.grid(column=0, row=1, padx=20, pady=20, sticky=W)
        self._style_button(reset_btn)
        exit_btn = Button(lower_section)
        exit_btn.configure(command=root.destroy, text="EXIT")
        exit_btn.grid(column=1, row=1, padx=20, pady=20, sticky=E)
        self._style_button(exit_btn)

        self._info_value = StringVar(value="")
        info_banner = Label(lower_section, textvariable=self._info_value)
        info_banner.grid(column=0, row=0, columnspan=2, sticky=(N, E, S, W))
        info_banner.configure(font=("Arial", 48), bg="#536878")

    def _reset_game(self) -> None:
        self._controller.reset_game()
        self._info_value.set("")

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
        self._controller.play(row, col)

    def handle_controller_change(self) -> None:
        self._draw_board()
        winner = self._controller.check_winner()
        if winner:
            self._handle_winner(winner)
        elif self._controller.is_tie():
            self._handle_tie()

    def _draw_board(self) -> None:
        i = 0
        for row in self._controller.get_game_board():
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
            self._info_value.set('Player "X" Has Won!')
        elif winner == TicTacToe.O:
            self._info_value.set('Player "O" Has Won!')

    def _handle_tie(self) -> None:
        self._info_value.set("The Game Ends In a Tie!")
