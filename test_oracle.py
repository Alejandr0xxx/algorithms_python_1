from oracle import *
from square_board import *

def test_base_oracle():
    board = SquareBoard.fromList(
        [
            [None, None, None, None],
            ["x", "o", "x", "o"],
            ["o", "o", "x", "x"],
            ["o", None, None, None],
        ]
    )
    expected = [
        RowRecommendation(0, RowClassification.MAYBE),
        RowRecommendation(1, RowClassification.FULL),
        RowRecommendation(2, RowClassification.FULL),
        RowRecommendation(3, RowClassification.MAYBE)
    ]
    
    test = BaseOracle.get_recommendations(board)
    assert len(test) == len(expected)
    assert test == expected
