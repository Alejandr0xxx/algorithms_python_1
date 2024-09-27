from player import Player
from match import Match

peter = None
otto = None

def setup():
    global peter, otto
    peter = Player("Peter")
    otto = Player("Otto")

def teardown():
    global peter, otto
    peter = None
    otto = None

def test_different_players_have_different_chars():
    t = Match(peter, otto)
    assert peter.char != otto.char


def test_no_player_with_none_char():
    t = Match(peter, otto)
    assert peter.char != None
    assert otto.char != None


def test_next_player_is_round_robbin():
    t = Match(peter, otto)
    p1 = t.next_player()
    p2 = t.next_player()
    assert p1 != p2

def test_players_are_opponents():
    t = Match(peter, otto)
    p1 = t.get_player('x')
    p2 =t.get_player('o')
    assert t.get_player("y") == 'Not Found'
    assert p1._opponent == p2
    assert p2._opponent == p1
