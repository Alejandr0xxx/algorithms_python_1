from oracle import BaseOracle, RowClassification, RowRecommendation, SmartOracle
import random
from beautifultable import BeautifulTable
from global_settings import *

class Player:
    def __init__(self, name, char=None, oracle=BaseOracle(), opponent=None):
        self.name = name
        self.char = char
        self._oracle = oracle
        self._opponent = opponent

    @property
    def opponent(self):
        return self._opponent

    @opponent.setter
    def opponent(self, opponent):
        if opponent != None:
            self._opponent = opponent
            opponent._opponent = self

    def play(self, board, player):
        (bestOption, recommendations) = self._ask_oracle(board, player)
        if bestOption is not None:  
            return self._play_on(board, bestOption.index)
        else:
            raise Exception(f"Could not find best option")

    def _ask_oracle(self, board, player):
        recommendations = self._oracle.get_recommendations(board, player)
        bestOption = self._chose(recommendations)
        if recommendations is not None:
            return (bestOption, recommendations)
        return None

    def _play_on(self, board, position):
        board.add(self.char, position)
        return board

    def _chose(self, recommendations):
        filtered_recommendations = list(
            filter(
                lambda r: r.recommendation != RowClassification.FULL, recommendations
            )
        )
        # ORDER BY CLASSIFICATION VALUE
        if filtered_recommendations:
            max_recommendation = max(
                filtered_recommendations, key=lambda r: r.recommendation.value
            )
            if max_recommendation.recommendation == RowClassification.WIN:
                return max_recommendation
            else:
                return random.choice(filtered_recommendations)
        return None

    # DUNDERS
    def __str__(self) -> str:
        return f"{self.name}"


class HumanPlayer(Player):
    def __init__(self, name, char=None):
        super().__init__(name, char)

    def _ask_oracle(self, board, player):
        while True:
            tmp_oracle = SmartOracle()
            raw = input(f"Select a column between 0 and {len(board) - 1} (h for help): ").strip()
            if raw == 'h':
                recommendations = ([tmp_oracle.get_recommendation(board, i, self) for i in range(len(board))])
                bt = BeautifulTable()
                bt.rows.append([rec[0] for rec in recommendations])
                bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
                print(bt)
                continue
            
            if not _is_int(raw):
                print("Please enter a column number")
                continue            
            
            raw = int(raw)
            
            if raw not in range(len(board)):
                print("Please enter a valid column number")
                continue
            
            if (
                _is_non_full_row(board, raw)
                and _is_within_valid_row(board, raw)
            ):
                return (RowRecommendation(raw, None), None)


# VALIDATION FUNCTIONS


def _is_within_valid_row(board, index):
    return index in range(len(board))


def _is_non_full_row(board, index):
    if not _is_within_valid_row(board, index):
        raise IndexError("Index out of bounds for the board.")
    return any([board.get_row(index).get_col(i) is None for i in range(len(board))])


def _is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
