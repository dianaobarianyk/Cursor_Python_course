import unittest
from unittest.mock import patch
from game import TicTacToe


class TestWinner(unittest.TestCase):

    def setUp(self):
        self.game_example = TicTacToe()

    def test_winner_row_id(self):
        self.game_example.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.assertTrue(self.game_example.winner(3, 'X'))
        self.game_example.print_board()
        self.game_example.board = [' ', ' ', ' ', 'X', 'O', 'X', ' ', ' ', ' ']
        self.assertFalse(self.game_example.winner(0, 'O'))
        self.game_example.print_board()

    def test_winner_column_id(self):
        self.game_example.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game_example.winner(0, 'X'))
        self.game_example.print_board()
        self.game_example.board = [' ', 'X', ' ', ' ', 'O', ' ', ' ', 'O', ' ']
        self.assertFalse(self.game_example.winner(1, 'O'))
        self.game_example.print_board()

    def test_winner_diagonal(self):
        self.game_example.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game_example.winner(0, 'X'))
        self.game_example.print_board()
        self.game_example.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.assertTrue(self.game_example.winner(2, 'X'))
        self.game_example.print_board()

    if __name__ == '__main__':
        unittest.main()
