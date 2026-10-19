from tkinter import E, Frame, N, S, Tk, W

from board_tile_gui import BoardTileGUI
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

        self._tiles: list[BoardTileGUI] = []
        padx = 5
        pady = 5
        for i in range(3):
            for j in range(3):
                new_tile = BoardTileGUI(i, j, 128, self._board)
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
                    lambda e, tile=new_tile: self._tile_clicked(tile)
                )


    def _tile_clicked(self, tile: BoardTileGUI) -> None:
        row = tile.get_row()
        col = tile.get_col()
        print(f"Clicked: row={row} col={col}")
        self._play(row, col)

    def _play(self, row:int, col:int) -> None:
        try:
            self._game_board.play(row, col)
            self._draw_board()
            winner = self._game_board.check_winner()
            if winner:
                print(f"player {winner} has won")
            print("succesful play")
        except ValueError as e:
            print(f"ValueError: {e}")

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

