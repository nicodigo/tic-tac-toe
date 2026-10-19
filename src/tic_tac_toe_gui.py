from tkinter import E, Frame, N, S, Tk, W

from tic_tac_toe import TicTacToe


class TicTacToeGUI:
    def __init__(self, root: Tk, game_board: TicTacToe) -> None:
        self._game_board = game_board
        root.title("Tic-Tac-Toe")
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        self._mainframe = Frame(root)
        self._mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self._mainframe.grid_columnconfigure(0, weight=1)
        self._mainframe.grid_rowconfigure(0, weight=1)

        self._board = Frame(self._mainframe)
        self._board.configure(bg='black')
        self._board.grid(column=0, row=0, sticky=(N, W, E, S))
        self._board.grid_columnconfigure([0, 1, 2], weight=1)
        self._board.grid_rowconfigure([0, 1, 2], weight=1)

        self._tiles: list[Frame] = []
        padx = 5
        pady = 5
        for i in range(3):
            for j in range(3):
                new_tile = Frame(self._board)
                new_tile.grid(row=i, column=j, sticky=(N, W, E, S))
                new_tile.configure(bg='white')

                if i == 0:
                    new_tile.grid_configure(pady=(0,pady))
                elif i == 2:
                    new_tile.grid_configure(pady=(pady, 0))
                else:
                    new_tile.grid_configure(pady=pady)

                if j == 0:
                    new_tile.grid_configure(padx=(0,padx))
                elif j == 2:
                    new_tile.grid_configure(padx=(padx, 0))
                else:
                    new_tile.grid_configure(padx=padx)

                self._tiles.append(new_tile)

                new_tile.bind(
                    '<Button-1>',
                    lambda e, row=i, col=j: self._tile_clicked(row, col)
                )


    def _tile_clicked(self, row: int, col: int) -> None:
        print(f"Clicked: row={row} col={col}")
        self._play(row, col)

    def _play(self, row:int, col:int) -> None:
        try:
            self._game_board.play(row, col)
        except ValueError as e:
            print(f"ValueError: {e}")
