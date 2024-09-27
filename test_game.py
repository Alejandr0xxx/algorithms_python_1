from game import *
from square_board import SquareBoard


def test_creation():
    g = Game()
    assert g != None


def test_is_game_over():
    game = Game()
    win_x = SquareBoard.fromList(
        [
            ["x", None, "x", None],
            ["o", "x", "o", "x"],
            [None, None, "x", "o"],
            ["o", "x", "o", None],
        ]
    )
    win_o = SquareBoard.fromList(
        [
            ["x", None, "x", None],
            ["o", None, "o", "x"],
            [None, "o", "x", "o"],
            ["o", "x", "o", None],
        ]
    )
    is_tie = SquareBoard.fromList(
        [
            ["x", "o", "x", "o"],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["o", "x", "o", "x"],
        ]
    )
    unfinised = SquareBoard.fromList(
        [
            ["x", "o", None, None],
            ["x", None, "x", None],
            [None, "o", "x", None],
            [None, "o", None, None],
        ]
    )
    game.board = win_x
    assert game._is_game_over('x') == True
    game.board = win_o
    assert game._is_game_over('o') == True
    game.board = is_tie  # this board is a tie, but the game is not over yet, so it should return False
    assert game._is_game_over('x') == True
    game.board = unfinised  # this board is not over yet, so it should return False
    assert game._is_game_over('x') == False