from list_utils import *
def test_find_streak():
    assert find_streak([1,1,1,4,5,6],1,3) == True
    assert find_streak([1,1,3,4,5,6],1,3) == False
    assert find_streak([1,1,3,1,1,1],1,3) == True
    assert find_streak([4,2,1,1,1,6],1,3) == True
    assert find_streak([1,1,1,1,1,1],1,3) == True
    assert find_streak([1,1,2,1,2,1],1,3) == False

