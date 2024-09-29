from square_board import *


def test_empty_square_board():
    empty = SquareBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory("o") == False


def test_horizontal_victory():
    horizontal = SquareBoard().fromList(
        [
            ["x", "o", "o", "o"],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ]
    )
    assert horizontal._any_horizontal_victory("x") == False
    assert horizontal._any_horizontal_victory("o") == True


def test_vertical_victory():
    vertical = SquareBoard().fromList(
        [
            ["x", None, "o", None],
            ["x", None, None, None],
            ["x", None, None, None],
            [None, None, None, None],
        ]
    )
    assert vertical._any_vertical_victory("x") == True
    assert vertical._any_vertical_victory("o") == False


def test_sinking_victory():
    sinking = SquareBoard().fromList(
        [
            [None, None, "o", None],
            [None, "x", None, None],
            ["o", None, "x", None],
            ["x", None, "x", "x"],
        ]
    )
    assert sinking._any_sinking_victory("x") == True
    assert sinking._any_sinking_victory("o") == False


def test_rising_victory():
    rising = SquareBoard().fromList(
        [
            [None, None, "o", None],
            ["x", "o", None, None],
            ["o", None, None, None],
            ["x", None, "x", None],
        ]
    )
    assert rising._any_rising_victory("x") == False
    assert rising._any_rising_victory("o") == True


def test_board_codes():
    board = SquareBoard.fromList(
        [
            ["x", "x", None, None],
            ["o", "o", None, "x"],
            ["x", "x", None, None],
            ["o", "o", None, "x"],
        ]
    )
    
    code = board.as_code()
    clone_board = SquareBoard.FromBoardCode(code)
    
    assert clone_board == board
    assert clone_board.as_code == code
    assert clone_board._as_code().raw_code == code.raw_code