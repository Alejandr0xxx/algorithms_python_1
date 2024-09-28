from global_settings  import BOARD_LENGTH, VICTORY_STRIKE
from list_utils import *
class LinearBoard:
    """
    A class representing a linear board
    x player 1
    o player 2
    None empty place
    """
    @classmethod
    def fromList(cls, list):
        if len(list)!= BOARD_LENGTH:
            raise ValueError(f'List length must be equal to {BOARD_LENGTH}, but got {len(list)}') 
        board = cls()
        board._row = list
        return board
    def __init__(self):
        """empty list"""
        self._row = [None for _ in range(BOARD_LENGTH)]

    def add(self, char):
        """add value to the board"""
        if self.is_full():
            return False
        i = self._row.index(None)
        self._row[i] = char
    
    def is_full(self):
        return len(self._row) == BOARD_LENGTH and not None in self._row   
    
    def is_empty(self):
            return all([x is None for x in self._row])
    
    def is_victory(self, char):
        return find_streak(self._row, char, VICTORY_STRIKE)
    
    def is_tie(self, char1, char2):
        return (self.is_victory(char1) == False) and (self.is_victory(char2)== False) 
    
    def __iter__(self):
        return iter(self._row)
    
    def get_col(self, index):
        return self._row[index]
    
    #DUNDERS 
    def __eq__(self, other: object) -> bool:
        if isinstance(other, LinearBoard):
            return self._row == other._row

    def __hash__(self) -> int:
        return hash(self._row)

    def __str__(self) -> str:
        return self._row.__str__()
    