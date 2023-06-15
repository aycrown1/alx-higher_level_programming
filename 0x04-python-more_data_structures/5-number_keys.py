#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        int: The number of keys in the dictionary.
    """
    keys = a_dictionary.keys()
    num_keys = len(keys)
    return num_keys
