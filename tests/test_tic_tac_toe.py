import unittest

from src.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_X_starts_playing(self):
        game = TicTacToe()
        game = game.play(0,0)
        self.assertEqual(
            game.get_board()[0][0],
            TicTacToe.X,
        )

    def test_change_turns_after_playing(self):
        game = TicTacToe()
        game = game.play(0,0)
        game = game.play(2,2)
        self.assertEqual(
            game.get_board()[2][2],
            TicTacToe.O,
        )

    def test_playing_in_not_empty_cell_raises_error(self):
        game = TicTacToe()
        game = game.play(0,0)
        self.assertRaises(ValueError, game.play, 0, 0)

    def test_no_winner_returns_none(self):
        game = TicTacToe()
        game = game.play(0,0)
        game = game.play(2,2)
        self.assertEqual(
            game.check_winner(),
            None,
        )

    def test_can_win_in_diagonal(self):
        game = TicTacToe()
        game = game.play(0,0) # X
        game = game.play(1,2)
        game = game.play(1,1) # X
        game = game.play(0,2)
        game = game.play(2,2) # X
        self.assertEqual(
            game.check_winner(),
            TicTacToe.X,
        )

    def test_can_win_in_column(self):
        game = TicTacToe()
        game = game.play(1,0) # X
        game = game.play(0,2)
        game = game.play(1,1) # X
        game = game.play(2,2)
        game = game.play(1,2) # X
        self.assertEqual(
            game.check_winner(),
            TicTacToe.X,
        )
    def test_can_win_in_row(self):
        game = TicTacToe()
        game = game.play(1,0) # X
        game = game.play(0,2)
        game = game.play(1,2) # X
        game = game.play(0,1)
        game = game.play(2,2) # X
        game = game.play(0,0)
        self.assertEqual(
            game.check_winner(),
            TicTacToe.O,
        )

    def test_is_tie_returns_true_if_no_winner(self):
        game = TicTacToe()
        game = game.play(0,0) # X
        game = game.play(0,1)
        game = game.play(0,2) # X
        game = game.play(1,1)
        game = game.play(1,0) # X
        game = game.play(1,2)
        game = game.play(2,1) # X
        game = game.play(2,0)
        game = game.play(2,2) # X
        self.assertTrue(game.is_tie())

    def test_equality_returns_true_if_equal(self):
        game1 = TicTacToe()
        game2 = TicTacToe()
        game1 = game1.play(0,0)
        game2 = game2.play(0,0)
        game1 = game1.play(2,2)
        game2 = game2.play(2,2)
        self.assertEqual(
            game1,
            game2
        )

    def test_equality_returns_false_if_not_equal(self):
        game1 = TicTacToe()
        game2 = TicTacToe()
        game1 = game1.play(0,0)
        game2 = game2.play(0,0)
        game1 = game1.play(2,2)
        self.assertNotEqual(
            game1,
            game2
        )


if __name__ == "__main__":
    unittest.main()
