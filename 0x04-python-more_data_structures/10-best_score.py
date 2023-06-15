#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value from a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        str or None: The key with the biggest
        integer value, or None if no score is found.
    """
    max_score = float('-inf')
    max_key = None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score:
            max_score = value
            max_key = key

    return max_key
