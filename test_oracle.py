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

    # def test_is_winning_move():
    #     p1 = Player('Don Pollo', 'x', oracle=None)
    #     p2 = Player('DalasRiviu', 'o', oracle=None)
        
    #     emptyBoard = SquareBoard()
    #     almost = SquareBoard.fromList([
    #         ['x', None, 'x', 'o'],
    #         ['o', None, None, None],
    #         [None, None, None, None],
    #         [None, None, None, None], 
    #     ])
    #     oracle = SmartOracle()
    #     for i in range(0, len(emptyBoard)): 
    #         assert oracle._is_winning_move(emptyBoard, i, p1) == False
    #         assert oracle._is_winning_move(emptyBoard, i, p2) == False
        
    #     for i in range(0, len(almost)):
    #         assert oracle._is_winning_move(almost, i, p1) == True
    #         assert oracle._is_winning_move(almost, i, p2) == False

# def test_play_on_temp_board():
#     board = SquareBoard.fromList(
#         [
#             [None, None, None, None],
#             ["x", "o", "x", "o"],
#             ["o", "o", "x", "x"],
#             [None, None, None, None],
#         ]
#     )
#     board2 = SquareBoard.fromList(
#         [
#             [None, None, None, None],
#             ["x", "o", "x", "o"],
#             ["o", "o", "x", "x"],
#             [None, 'x', None, None],
#         ]
#     )

#     oracle = SmartOracle()
#     assert oracle.play_on_temp_board(board, 1, Player('A', 'x')).get_row(1) == board2.get_row(1)
# def test_smart_oracle_recommend_maybe():
#     board = SquareBoard.fromList(
#         [
#             ['x', 'o', None, None],
#             ['o', 'x', None, None],
#             ['x', 'x', None, None],
#             ['o', None, None, None],
#         ]
#     )
#     oracle = SmartOracle()
#     player = Player('A', 'x')
#     player.opponent = Player('B', 'o')
#     recommendations = [oracle.get_recommendation(board, i, player) for i in range(BOARD_LENGTH)]
    
#     # Debemos obtener al menos una recomendación MAYBE (posible jugada) en el tablero.
#     winner_move = [(classification, index) for (classification, index) in recommendations if classification == 100][0]
    
#     assert winner_move, "El SmartOracle no recomendó una jugada posible en una fila con espacio."

def test_is_BAD_move():
    board = SquareBoard.fromList(
        [
            ['x', 'o', 'o', None],
            ['o', 'x', None, None],
            ['x', 'o', None, None],
            ['o', None, None, None],
        ]
    )
    oracle = SmartOracle()
    player = Player('A', 'x')
    playeropponent = Player('B', 'o')
    player.opponent = playeropponent
    assert oracle._is_losing_move(board, 1, player) == True

def test_no_good_options():
    x = Player('Otto', char='x')
    o = Player('Xavier', char='o', opponent=x)
    
    oracle = MemoizingOracle()
    
    maybe = SquareBoard.FromBoardCode('....|x...|....|....')
    bad_and_full = SquareBoard.FromBoardCode('x...|oo..|o...|xoxo')
    all_bad = SquareBoard.From('x...|oo..|o...|....')
    assert oracle.no_good_options(maybe, x) == False
    assert oracle.no_good_options(bad_and_full, x)
    assert oracle.no_good_options(all_bad, x)