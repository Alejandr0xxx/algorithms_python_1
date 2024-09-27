from oracle import BaseOracle, RowClassification


class Player:
    def __init__(self, name, char=None, oracle=BaseOracle, opponent=None):
        self.name = name
        self.char = char
        self._oracle = oracle
        self.opponent = opponent

    @property
    def opponent(self):
        return self._opponent
    
    @opponent.setter
    def opponent(self, opponent):
        if opponent != None:
            self._opponent = opponent
            opponent._opponent = self
    
    def play(self, board):
        (bestOption, recommendations) = self._ask_oracle(board)
        if bestOption is not None:
            return self._play_on(board, bestOption)
        else:
            raise Exception(f"Could not find best option")

    def _ask_oracle(self, board):
        recommendations = self._oracle.get_recommendations(board)
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
        if filtered_recommendations:
            return filtered_recommendations[0].index
        return None

    #DUNDERS 
    def __str__(self) -> str:
        return f"{self.name}"

class HumanPlayer(Player):
    def __init__(self, name, char=None):
        super().__init__(name, char)

    # def _ask_oracle(self, board):

    #     while True:
    #         raw = int(input(f'Select a column between 0 and {len(board)}'))
    #         if _is_int(raw) and _is_non_full_row(board, raw) and _is_within_valid_row(board, raw):
    #             return (RowRecommendation(raw, None), None)


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