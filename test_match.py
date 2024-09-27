from player import Player, HumanPlayer
from match import Match
import pytest
@pytest.fixture
def players():
    peter = Player("Peter")
    otto = Player("Otto")
    return peter, otto

def test_different_players_have_different_chars(players):
    peter, otto = players
    t = Match(peter, otto)
    assert peter.char != otto.char


def test_no_player_with_none_char(players):
    peter, otto = players
    t = Match(peter, otto)
    assert peter.char != None
    assert otto.char != None


def test_next_player_is_round_robbin(players):
    peter, otto = players
    t = Match(peter, otto)
    p1 = t.next_player
    p2 = t.next_player
    assert p1 != p2

def test_players_are_opponents(players):
    peter, otto = players
    t = Match(peter, otto)
    p1 = t.get_player('x')
    p2 =t.get_player('o')
    assert t.get_player("y") == 'Not Found'
    assert p1._opponent == p2
    assert p2._opponent == p1
