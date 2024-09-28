from enum import Enum
from copy import deepcopy
import random


class RowClassification(Enum):
    FULL = -1
    MAYBE = 1
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
        is_full_or_not = self.is_full_or_not(board, index)
        return RowRecommendation(index, is_full_or_not)

    def is_full_or_not(self, board, index):
        if None in board.get_row(index):
            return RowClassification.MAYBE
        return RowClassification.FULL


class SmartOracle(BaseOracle):
    def recommend(self, board, index, player):
        """
        Obtiene las recomendaciones del oráculo, filtrando las que no están llenas y buscando posibles movimientos ganadores.
        """
        recommendations = super().get_recommendations(board, index, player)
        # Filtrar las recomendaciones que tienen espacio (MAYBE)
        maybe_recommendations = [
            rec
            for rec in recommendations
            if rec.recommendation != RowClassification.FULL
        ]
        if maybe_recommendations:
            winning_move = self._is_winning_move(board, index, player)
        return winning_move

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
