from square_board import SquareBoard
from oracle import BaseOracle
from player import Player
def test_play():
    """Comprobar que se juega en la primera columna"""

    before = SquareBoard.fromList(
        [
            [None, None, None, None],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", None, None, None],
        ]
    )
    after = SquareBoard.fromList(
        [
            ['o', None, None, None],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", None, None, None],
        ]
    )
    player = Player('Alejandr0x', 'x', oracle= BaseOracle)
    
    assert player.play(before) == after