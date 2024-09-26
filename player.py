from oracle import BaseOracle
class Player:
    def __init__(self, name, char, oracle = BaseOracle()):
        self.name = name
        self.char = char
        self._oracle = oracle
    
    def play(self, board):
        pass
    
    
    
    def _chose(self, recommendations):
        pass