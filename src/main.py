from tkinter import Tk

from tic_tac_toe import TicTacToe
from tic_tac_toe_gui import TicTacToeGUI


def main() -> None:
    root = Tk()
    game = TicTacToe()
    game_wind = TicTacToeGUI(root, game)
    root.mainloop()


if __name__ == "__main__":
    main()
