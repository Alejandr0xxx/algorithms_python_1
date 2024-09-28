from square_board import SquareBoard
from oracle import BaseOracle, RowRecommendation, RowClassification
from player import Player, _is_within_valid_row, _is_non_full_row, _is_int


# def test_play():
#     """Comprobar que se juega en la primera columna"""

#     before = SquareBoard.fromList(
#         [
#             [None, None, None, None],
#             ["x", "o", "x", "o"],
#             ["o", "x", "o", "x"],
#             ["x", None, None, None],
#         ]
#     )
#     after = SquareBoard.fromList(
#         [
#             ["x", None, None, None],
#             ["x", "o", "x", "o"],
#             ["o", "x", "o", "x"],
#             ["x", None, None, None],
#         ]
#     )
#     player = Player("Alejandr0x", "x", oracle=BaseOracle)

#     assert player.play(before) == after


def test_valid_row():

    board = SquareBoard.fromList(
        [
            ["x", None, None, None],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", None, None, None],
        ]
    )

    assert _is_within_valid_row(board, 0)
    assert _is_within_valid_row(board, 1)
    assert _is_within_valid_row(board, 2)
    assert _is_within_valid_row(board, 3)
    assert _is_within_valid_row(board, 4) == False
    assert _is_within_valid_row(board, -5) == False
    assert _is_within_valid_row(board, 6) == False


def test_is_non_full_row():
    board = SquareBoard.fromList(
        [
            ["x", None, None, None],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", None, None, None],
        ]
    )
    assert _is_non_full_row(board, 0)
    assert _is_non_full_row(board, 1) == False
    assert _is_non_full_row(board, 2) == False
    assert _is_non_full_row(board, 3)


def test_is_int():
    assert _is_int("0")
    assert _is_int("5")
    assert _is_int("1.5") == False
    assert _is_int("-2")
    assert _is_int("      3       ")
    assert _is_int("") == False


def test_chose_max():
    p = Player("a", "x")
    recommendations = [
        RowRecommendation(1, RowClassification.FULL),
        RowRecommendation(4, RowClassification.MAYBE),
        RowRecommendation(2, RowClassification.WIN),
        RowRecommendation(3, RowClassification.MAYBE),
        RowRecommendation(2, RowClassification.FULL),
    ]
    assert p._chose(recommendations) == RowRecommendation(2, RowClassification.WIN)
