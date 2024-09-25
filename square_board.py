from linear_board import LinearBoard
from global_settings import *
class SquareBoard:
    
    @classmethod
    def fromList(cls, list_of_list):
        """"Transform the list of list into a square board"""
        board = cls()
        board.board = list(map(lambda x: LinearBoard.fromList(x), list_of_list))
        return board
    
    def __init__(self):
        self.board = [LinearBoard() for _ in range(BOARD_LENGTH)]
    
    def is_empty(self):
        return all(b.is_empty() for b in self.board)
    
    def is_full(self):
        return all(b.is_full() for b in self.board)

    def is_victory(self, char):
        return self._any_horizontal_victory(char) or self._any_vertical_victory() or self._any_sinking_victory() or self._any_rising_victory()    

    def _any_horizontal_victory(self, char):
        return any(b.is_victory(char) for b in self.board)
    
    def _any_vertical_victory(self):
        return False
    
    def _any_sinking_victory(self):
        return False
    
    def _any_rising_victory(self):
        return False

    #DUNDERS

    def __repr__(self) -> str:
        return f'{self.__class__}: {self.board}'