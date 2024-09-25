import pytest
from linear_board import *
from .settings import *

# Test the function to initialize the board
def test_empty_board():
    empty = LinearBoard()
    assert empty != None
    assert empty.is_full() == False
    assert empty.is_victory('x') == False

def test_add():
    b = LinearBoard()
    for _ in range(BOARD_LENGTH):
        b.add('x')
    assert b.is_full() == True

def test_victory():
    b = LinearBoard()
    for _ in range(VICTORY_STRIKE):
        b.add('x')
    
    assert b.is_victory('o') == False
    assert b.is_victory('x') == True


def test_tie():
    b = LinearBoard()
    
    b.add('o')
    b.add('o')
    b.add('x')
    b.add('o')
    
    assert b.is_tie('o', 'x')


def test_add_to_full_board():
    b = LinearBoard()
    for _ in range(BOARD_LENGTH + 1):
        b.add('x')

    assert b.is_full