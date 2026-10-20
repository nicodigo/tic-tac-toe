from tkinter import Tk

from tic_tac_toe import TicTacToe
from tic_tac_toe_gui import TicTacToeGUI


def is_one_player_mode() -> bool:
    option = -1

    while option != 1 and option != 2:
        try:
            option = int(input("Select (1) For One Player Mode or (2) For Two Player Mode: "))
        except ValueError:
            print("Must enter a numeric value (1 / 2)")
    return option == 1


def get_bot_symbol() -> int:
    option = -1

    while option != TicTacToe.X and option != TicTacToe.O:
        symbol = input("Select the symbol that **The Bot** will use (X / O): ")
        if symbol.lower() == "x":
            option = TicTacToe.X
        elif symbol.lower() == "o":
            option = TicTacToe.O
        else:
            print("error: you must choose between 'X' and 'O'")

    return option



def main() -> None:
    one_player_mode: bool = is_one_player_mode()
    root = Tk()
    game = TicTacToe()
    if one_player_mode:
        print("one player mode selected")
        bot_symbol = get_bot_symbol()
        game_wind = TicTacToeGUI(root, game, one_player_mode, bot_symbol)
    else:
        game_wind = TicTacToeGUI(root, game)
    root.mainloop()


if __name__ == "__main__":
    main()
