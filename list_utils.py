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

def collapse_list(lst):
    return ''.join(x if x != None else '.' for x in lst)

def collapse_matrix(matrix):
    return '|'.join(collapse_list(row) for row in matrix)

def replace_all(lst, old, new):
    return [x if x != old else new for x in lst]

def replace_all_in_matrix(matrix, old, new):
    return [replace_all(row, old, new) for row in matrix if row != []]