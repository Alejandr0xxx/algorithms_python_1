from list_utils import *
def test_find_streak():
    assert find_streak([1,1,1,4,5,6],1,3) == True
    assert find_streak([1,1,3,4,5,6],1,3) == False
    assert find_streak([1,1,3,1,1,1],1,3) == True
    assert find_streak([4,2,1,1,1,6],1,3) == True
    assert find_streak([1,1,1,1,1,1],1,3) == True
    assert find_streak([1,1,2,1,2,1],1,3) == False

def test_first_elements():
    original = [[9,8,7],[6,5,4],[3,2,1]]
    assert transpose_elements(original) == [[9,6,3], [8,5,2], [7,4,1]]