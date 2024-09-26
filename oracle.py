from enum import Enum

class RowClassification(Enum):
    FULL = 'FULL'
    MAYBE = 'MAYBE'

class BaseOracle:
    @staticmethod
    def get_recommendations(board):
        return [RowRecommendation.recommend(i, row) for i, row in enumerate(board)]

class RowRecommendation():
    def __init__(self, index, recommendation):
        self.index = index
        self.recommendation = recommendation
    
    @staticmethod
    def recommend(index, row):
        is_full_or_not = RowRecommendation.is_full_or_not(row)
        return  RowRecommendation(index, is_full_or_not)
    @staticmethod
    def is_full_or_not(row):
        if any(x is None for x in row):
            return RowClassification.MAYBE
        return RowClassification.FULL
    
    #DUNDERS 
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.index}, {self.recommendation})"

    def __eq__(self, other):
        if isinstance(other, RowRecommendation):
            return self.index == other.index and self.recommendation == other.recommendation
        return False
    
    def __hash__(self) -> int:
        return hash((self.index, self.recommendation))