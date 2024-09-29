from enum import Enum
from copy import deepcopy
import random
from global_settings import *


class RowClassification(Enum):
    FULL = -1
    BAD = 1
    MAYBE = 10
    BLOCK_OPPONENT = 30
    WIN = 100


class RowRecommendation:
    def __init__(self, index, recommendation):
        self.index = index
        self.recommendation = recommendation

    # DUNDERS

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.index}, {self.recommendation})"

    def __eq__(self, other):
        if isinstance(other, RowRecommendation):
            return (
                self.index == other.index
                and self.recommendation == other.recommendation
            )
        return False

    def __hash__(self) -> int:
        return hash((self.index, self.recommendation))


class BaseOracle:
    def get_recommendations(self, board, player):
        """
        Genera recomendaciones basadas en si las filas del tablero están llenas o tienen espacio (MAYBE).
        """
        return [self.recommend(board, i, player) for i in range(len(board))]

    def recommend(self, board, index, player):
        # Revisar si la fila está llena o no
        recommendation = self.is_full_or_not(board, index)
        return RowRecommendation(index, recommendation)

    def is_full_or_not(self, board, index):
        if None in board.get_row(index):
            return RowClassification.MAYBE
        return RowClassification.FULL


class SmartOracle(BaseOracle):
    def get_recommendation(self, board, index, player):
        """
        Obtiene las recomendaciones del oráculo, filtrando las que no están llenas y buscando posibles movimientos ganadores.
        """
        if self._is_winning_move(board, index, player):
            return RowRecommendation(index, RowClassification.WIN)
        elif self._block_opponent_winning_move(board, player):
            return RowRecommendation(index, RowClassification.BLOCK_OPPONENT)
        elif self._is_losing_move(board, index, player):
            return RowRecommendation(index, RowClassification.BAD)
        else:
            return RowRecommendation(index, RowClassification.MAYBE)

    def _is_losing_move(self, board, index, player):
        """ "If player plays at index, he might lose next turn"""
        tmp_board = self.play_on_temp_board(board, index, player)
        BAD = False
        for i in range(BOARD_LENGTH):
            if self._is_winning_move(tmp_board, i, player._opponent):
                BAD = True
                break
        return BAD

    def _block_opponent_winning_move(self, board, player):
        for i in range(BOARD_LENGTH):
            if self._is_winning_move(board, i, player._opponent):
                return True
        return False

    def _is_winning_move(self, board, index, player):
        """
        Simula un movimiento en el tablero temporal para verificar si resulta en una victoria.
        """
        tmp_board = self.play_on_temp_board(board, index, player)
        return tmp_board.is_victory(player.char)

    def play_on_temp_board(self, board, index, player):
        """
        Simula jugar en un tablero temporal, para predecir el resultado del movimiento.
        """
        tmp_board = deepcopy(board)
        tmp_board.add(player.char, index)
        return tmp_board


class MemoizingOracle(SmartOracle):
    def __init__(self):
        super().__init__()
        self._past_recommendations = {}

    def _make_key(self, board, player):
        """
        Create a unique key for the board and player
        """
        return f"{board.as_code()}@{player.char}"

    def get_recommendation(self, board, index, player):
        """
        Create a key
        Look at cache
        If found, return the recommendation else save in cache
        """
        key = self._make_key(board, player)
        if key not in self._past_recommendations:
            self._past_recommendations[key] = super().get_recommendation(
                board, index, player
            )

        return self._past_recommendations[key]


class LearningOracle(MemoizingOracle):
    def update_to_bad(self, board_code, player, position):
        """
        If the player makes a bad move, update the cache for that board_code and player
        """
        key = self._make_key(board_code, player.char)
        if key in self._past_recommendations:
            self._past_recommendations[key][position] = RowRecommendation(
                position, RowClassification.BAD
            )
