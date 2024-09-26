from oracle import BaseOracle, RowClassification
class Player:
    def __init__(self, name, char, oracle = BaseOracle):
        self.name = name
        self.char = char
        self._oracle = oracle
    
    def play(self, board):
        recommendations = self._oracle.get_recommendations(board)
        bestOption = self._chose(recommendations)
        if bestOption is not None:
            board.add(self.char, bestOption)
        return board
    
    
    def _chose(self, recommendations):
        filtered_recommendatios =  list(filter(lambda r: r.recommendation != RowClassification.FULL, recommendations))
        if filtered_recommendatios:
            return filtered_recommendatios[0].index
        return None