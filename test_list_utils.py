from list_utils import *


def test_find_streak():
    assert find_streak([1, 1, 1, 4, 5, 6], 1, 3) == True
    assert find_streak([1, 1, 3, 4, 5, 6], 1, 3) == False
    assert find_streak([1, 1, 3, 1, 1, 1], 1, 3) == True
    assert find_streak([4, 2, 1, 1, 1, 6], 1, 3) == True
    assert find_streak([1, 1, 1, 1, 1, 1], 1, 3) == True
    assert find_streak([1, 1, 2, 1, 2, 1], 1, 3) == False


def test_collapse_list():
    assert collapse_list(["x", "o", "x", "x"]) == "xoxx"

    assert collapse_list([]) == ""
    assert collapse_list(["x", "x", None, None, None]) == "xx..."


def test_collapse_matrix():
    assert collapse_matrix([]) == ""
    assert (
        collapse_matrix([["o", "x", None], ["x", "o", "x"], [None, None, "o"]])
        == "ox.|xox|..o"
    )


def test_replace_all():
    assert replace_all([None, "25", 654, None, False], None, "#") == [
        "#",
        "25",
        654,
        "#",
        False,
    ]
    assert replace_all(["x", "o", "x", "x"], 1, 2) == ["x", "o", "x", "x"]
    assert replace_all([], "x", "y") == []


def test_replace_all_in_matrix():
    assert replace_all_in_matrix(
        [["o", "x", None], ["x", "o", "x"], [None, None, "o"]], None, "#"
    ) == [["o", "x", "#"], ["x", "o", "x"], ["#", "#", "o"]]
    assert replace_all_in_matrix(
        [["o", "x", None], ["x", "o", "x"], [None, None, "o"]], "aña", "#"
    ) == [["o", "x", None], ["x", "o", "x"], [None, None, "o"]]

    assert replace_all_in_matrix([], None, 0) == []
    assert replace_all_in_matrix([[], []],1,1) == []
