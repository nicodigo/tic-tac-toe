import unittest

from src.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_X_starts_playing(self):
        game = TicTacToe()
        game.play(0,0)
        self.assertEqual(
            game.get_board()[0][0],
            TicTacToe.X,
        )

if __name__ == "__main__":
    unittest.main()
