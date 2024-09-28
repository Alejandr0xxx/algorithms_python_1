import pyfiglet
from enum import Enum, auto
from match import Match
from player import Player, HumanPlayer
from square_board import SquareBoard
from beautifultable import BeautifulTable
from global_settings import *
from list_utils import *
from oracle import SmartOracle
class RoundType(Enum):
    COMPUTER_VS_COMPUTER = auto()
    HUMAN_VS_COMPUTER = auto()


class DifficultyLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class Game:
    def __init__(
        self,
        round_type=RoundType.COMPUTER_VS_COMPUTER,
        match=Match(Player("Arthur Morgan"), Player("Dutch Vanderlinde")),
    ):
        self._round_type = round_type
        self.match = match

        self.board = SquareBoard()

    def start(self):
        self.print_logo()

        # match config

        self._configure_match_by_user()

        self._start_game_loop()

        print("Game over!")

    def _configure_match_by_user(self):
        """
        Ask to user for match configuration (difficulty level and match type)
        """
        # Aks for match type
        self._round_type = self._get_round_type_from_user()
        if self._round_type == RoundType.HUMAN_VS_COMPUTER:
            self._difficulty_level = self._get_difficulty_level_from_user()
        self.match = self._make_match()
    
    def  _get_difficulty_level_from_user(self):
        print("Choose difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        while True:
            level = str(input("Enter your choice (1/3) ")).strip()
            if level not in str(range(1, 4)):
                print("Invalid choice. Please try again.")
                continue
            break
        return level
    def _start_game_loop(self):
        while True:
            curr_player = self.match.next_player
            curr_player.play(self.board, curr_player)
            self.display_move(curr_player)
            self.display_board()
            if self._is_game_over(curr_player.char) == 1:
                self.display_board
                print("Its a tie!")
                break
            elif self._is_game_over(curr_player.char) == 2:
                self.display_board()
                self.display_winner()
                break

    def display_winner(self):
        # Display the winner of the game
        print(f"{self.match.get_winner(self.board)} wins!")

    def display_move(self, player):
        print(f"{player.name} plays...")

    def display_board(self):
        matrix = self.board
        bt = BeautifulTable()
        for col in matrix:
            bt.columns.append(col)
        bt.columns.header = [str(i) for i in range(BOARD_LENGTH)]
        return print(bt)

        # print(self.board)
    
    def _is_game_over(self, char):
        # Check if game is over (board is full or someone has won)
        if self.board.is_full():
            return 1
        elif self.board.is_victory(char):
            return 2
        
    def _make_match(self):
        # Create match based on user's choice
        # Player 1 will always be the robot
        player1 = Player("Arthur Morgan" , oracle=SmartOracle)
        player2 = Player("Dutch Vanderlinder", oracle=SmartOracle)
        if self._round_type == RoundType.COMPUTER_VS_COMPUTER:
            return Match(player1, player2)
        elif self._round_type == RoundType.HUMAN_VS_COMPUTER:
            username = self._ask_for_name()
            player2 = HumanPlayer(username)
            return Match(player1, player2)
        else:
            print("Invalid match type. Exiting...")
            exit(0)

    def _ask_for_name(self):
        # Ask user for name
        while True:
            username = str(input("Enter your name: ")).strip()
            if username:
                return username
            else:
                print("Name cannot be empty. Please try again.")
                continue

    def _get_round_type_from_user(self):
        # Ask user for match type
        while True:
            print("Choose a game mode:")
            print("1. Computer vs Computer")
            print("2. Human vs Computer")
            print("3. Exit")
            choice = input("Enter your choice (1/3): ").strip()

            if choice == "1":
                return RoundType.COMPUTER_VS_COMPUTER
            elif choice == "2":
                return RoundType.HUMAN_VS_COMPUTER
            elif choice == "3":
                print("Exiting...")
                exit(0)
            else:
                print("Invalid choice. Please try again.")
                continue

    def print_logo(self):
        logo = pyfiglet.Figlet(font="stop")
        print(logo.renderText("Conecta"))
