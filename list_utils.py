def find_streak(lst, char, VICTORY_STRIKE):
    """
    Given a list of elements, return True if the list contains a sequence of
    VICTORY_STRIKE identical elements, otherwise return False.
    """
    for i in range(len(lst) - VICTORY_STRIKE + 1):
        if lst[i: i + VICTORY_STRIKE] == [char] * VICTORY_STRIKE:
            return True
    return False

def transpose_elements(lst):
    """TRANSPOSE FUNCT"""
    return [list(row) for row in zip(*lst)]
