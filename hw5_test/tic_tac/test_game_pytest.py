import pytest
from game import TicTacToe


def setup_module(module):
    global game_example
    game_example = TicTacToe()
    game_example.board[4] = "X"


def test_available_moves():
    assert (4 not in game_example.available_moves())


def test_make_move():
    assert not (game_example.make_move(4, "X"))
    assert (game_example.make_move(5, "X"))
    assert (game_example.board[5] != " ")
