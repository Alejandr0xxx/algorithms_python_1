from linear_board import LinearBoard
from global_settings import *
from list_utils import *


class SquareBoard:

    @classmethod
    def fromList(cls, list_of_list):
        """ "Transform the list of list into a square board"""
        if len(list_of_list) != BOARD_LENGTH:
            raise ValueError(
                f"Board length must be {BOARD_LENGTH} x {BOARD_LENGTH} but got {len(list_of_list)} x {len(list_of_list[0]) }"
            )
        board = cls()
        board.board = list(map(lambda x: LinearBoard.fromList(x), list_of_list))
        return board

    def __init__(self):
        self.board = [LinearBoard() for _ in range(BOARD_LENGTH)]

    def add(self, char, row):
        self.board[row].add(char)

    def is_empty(self):
        return all(r.is_empty() for r in self.board)

    def is_full(self):
        return all(r.is_full() for r in self.board)

    def is_victory(self, char):
        return (
            self._any_horizontal_victory(char)
            or self._any_vertical_victory(char)
            or self._any_sinking_victory(char)
            or self._any_rising_victory(char)
        )

    def _any_horizontal_victory(self, char):
        return any(r.is_victory(char) for r in self.board)

    def _any_vertical_victory(self, char):
        temp_board = [
            LinearBoard.fromList(
                [self.board[row].get_col(col) for row in range(BOARD_LENGTH)]
            )
            for col in range(BOARD_LENGTH)
        ]
        return any(r.is_victory(char) for r in temp_board)

    def get_row(self, index):
        return self.board[index]

    def _any_sinking_victory(self, char):
        for row in range(BOARD_LENGTH):
            for col in range(BOARD_LENGTH):
                if (col + VICTORY_STRIKE <= BOARD_LENGTH and row + VICTORY_STRIKE <= BOARD_LENGTH):
                    if (all(self.board[row + i].get_col(col + i) == char for i in range(VICTORY_STRIKE))):
                        return True
        return False
    def _any_rising_victory(self, char):
        for row in range(BOARD_LENGTH):
            for col in range(BOARD_LENGTH):
                if (col - (VICTORY_STRIKE - 1) >= 0 and row + VICTORY_STRIKE <= BOARD_LENGTH):
                    if all(self.board[row + i].get_col(col - i) == char for i in range(VICTORY_STRIKE)):
                        return True
        return False
    # DUNDERS
    def __repr__(self) -> str:
        return f"{self.__class__}: {self.board}"
    
    def __iter__(self) -> iter:
        return iter(self.board)


    def __eq__(self, other: object) -> bool:
        if isinstance(other, SquareBoard):
                return self.board == other.board
        return False

    def __hash__(self) -> int:
        return hash(self.board)

    def __len__(self) -> int:
        return len(self.board)
    
    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.board)