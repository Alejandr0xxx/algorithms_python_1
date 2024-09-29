from string_utils import *
def test_explode_string():
    assert explode_string("Hello,World!") == ["H","e","l","l","o",",","W", "o", "r", "l", "d", "!"]
    assert explode_string("") == []


def test_explode_list_of_strings():
    assert explode_list_of_strings(["Hello", ",", "World!"]) == [["H","e","l","l","o"],[","],["W", "o", "r", "l", "d", "!"]]
    assert explode_list_of_strings(["", ""]) == []
    assert explode_list_of_strings([]) == []