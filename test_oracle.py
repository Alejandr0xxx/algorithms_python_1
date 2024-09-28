from oracle import *
from square_board import *
from player import Player
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
    oracle = BaseOracle()
    test = oracle.get_recommendations(board, 'x')
    assert len(test) == len(expected)
    assert test == expected

def test_is_winning_move():
    p1 = Player('Don Pollo', 'x')
    p2 = Player('DalasRiviu', 'o')
    
    emptyBoard = SquareBoard()
    almost = SquareBoard.fromList([
        ['x', None, 'x', 'o'],
        ['o', None, None, None],
        [None, None, None, None],
        [None, None, None, None], 
    ])
    oracle = SmartOracle()
    for i in range(0, len(emptyBoard)):
        assert oracle._is_winning_move(emptyBoard, i, p1) == False
        assert oracle._is_winning_move(emptyBoard, i, p2) == False
    
    for i in range(0, len(almost)):
        assert oracle._is_winning_move(almost, i, p1) == True
        assert oracle._is_winning_move(almost, i, p2) == False