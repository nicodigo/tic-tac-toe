from tkinter import Tk

from controller import Controller
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
    game = TicTacToe()
    if one_player_mode:
        print("One Player Mode Selected")
        bot_symbol = get_bot_symbol()
        print("Bot symbol selected correctly")
        print("Initializing the game, it will take a few seconds...")
        ctrl: Controller = Controller(game, True, bot_symbol)
        print("I hope you have fun!!")
    else:
        print("Two Player Mode Selected")
        print("Initializing the game, it will take a few seconds...")
        ctrl: Controller = Controller(game, False)
        print("I hope you have fun!!")
    root = Tk()
    game_wind = TicTacToeGUI(root, ctrl)
    ctrl.set_game_state_change_callback(game_wind.handle_controller_change)
    root.mainloop()


if __name__ == "__main__":
    main()
