class Game:
    def __init__(self, board_size, player1, player2):
        self.board_size = board_size
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = player1
        self.players = [player1, player2]
    
    def start (self):
        pass