#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): The first input set.
        set_2 (set): The second input set.

    Returns:
        set: A set containing the elements present in only one of the two sets.
    """
    diff_set = set_1.symmetric_difference(set_2)

    return diff_set
