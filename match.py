class Match:
    def __init__(self, player1, player2):
        player1.char = 'x'
        player2.char = 'o'
        player1.opponent = player2
    
        self._players = {'x': player1, 'o': player2}
        self._round_robin = [player1, player2]
    @property
    def next_player(self):
        curr_player = self._round_robin[0]
        self._round_robin.reverse()
        return curr_player

    def get_winner(self, board):
        if board.is_victory('x'):
            return self._players['x']
        elif board.is_victory('o'):
            return self._players['o']
        else:
            return None
        
    
    def get_player(self, char):
        return self._players.get(char, 'Not Found')