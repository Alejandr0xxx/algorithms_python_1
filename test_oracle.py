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
    
    rappel = BaseOracle()
    assert len(rappel.get_recommendations(board)) == len(expected)
    assert rappel.get_recommendations(board) == expected
